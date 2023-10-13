import os
from django.shortcuts import render, redirect, get_object_or_404
from .models import Feedback, Portfolio
from .forms import FeedbackForm, OrderForm, CourseForm
from .convertation import convert_heic_to_png
from price.models import Service, ManicureType, Order
from courses.models import Course, CourseWrite
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


# Create your views here.
def index(request):
    feed_back = Feedback.objects.order_by('-create_date')
    portfolio = Portfolio.objects.order_by('-create_date')
    services = Service.objects.all()

    service_details = {}
    for service in services:
        manicure_types = ManicureType.objects.filter(service=service)
        service_details[service] = {'manicure_types': manicure_types, 'image': service.img.url}

    for item in portfolio:
        if item.img:  # Проверяем, что поле img не пустое
            _, file_extension = os.path.splitext(item.img.name)
            if file_extension.lower() == '.heic':
                base_directory = 'media'  # Базовый каталог, где хранятся изображения
                heic_filename = os.path.join(base_directory, item.img.name)

                # Создаем общую папку для всех сконвертированных изображений
                converted_images_directory = os.path.join(base_directory, 'images-slider')
                os.makedirs(converted_images_directory, exist_ok=True)  # Создаем директорию, если ее нет

                png_filename = os.path.join(converted_images_directory, f"{item.id}.png")

                if convert_heic_to_png(heic_filename, png_filename):
                    # Обновляем поле img объекта Portfolio, чтобы оно указывало на новый PNG файл
                    item.img.name = os.path.relpath(png_filename, base_directory)
                    item.save()  # Сохраняем объект Portfolio с обновленным полем img

                    # Удаляем оригинальный HEIC файл
                    os.remove(heic_filename)

    return render(request, 'main/index.html', {
        'feed_back': feed_back,
        'portfolio': portfolio,
        'services': services,
        'service_details': service_details,
    })


def about(request):
    return render(request, 'main/about.html')


def write(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            if (form.cleaned_data['manicure_types_service1'] or
                    form.cleaned_data['manicure_types_service2'] or
                    form.cleaned_data['manicure_types_service3']):
                form.save()
                return redirect('confirmed')
            else:
                form.add_error('manicure_types_service1', 'Выберите хотя бы один вид маникюра')
    else:
        form = OrderForm()

    return render(request, 'main/write.html', {
        'form': form,
    })


def feedback(request):
    error = ''

    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thanks')
        else:
            error = 'Заполните пожалуйста поле'

    form = FeedbackForm()

    data = {
        'form': form,
        'error': error,
    }

    return render(request, 'main/feedback.html', data)


def thanks(request):
    feed_back = Feedback.objects.order_by('-create_date')[0]

    return render(request, 'main/thanks.html', {'feed_back': feed_back})


def write_confirmed(request):
    order = Order.objects.order_by('-create_date')[0]

    return render(request, 'main/write_confirmed.html', {'order': order})


class CoursesView(ListView):
    model = Course
    template_name = 'main/courses.html'
    context_object_name = 'courses'


class CourseView(DetailView):
    model = Course
    template_name = 'main/course.html'
    context_object_name = 'course'


def write_course(request, course_slug):
    course = get_object_or_404(Course, slug=course_slug)

    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course-confirmed')

    form = CourseForm()

    return render(request, 'main/course_write.html', {
        'form': form,
        'course': course,
    })


def course_confirmed(request):
    order = CourseWrite.objects.order_by('-create_date')[0]

    return render(request, 'main/course_confirmed.html', {'order': order})
