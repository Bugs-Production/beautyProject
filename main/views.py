import os
from django.shortcuts import render, redirect
from .models import Feedback, Portfolio
from .forms import FeedbackForm
from .convertation import convert_heic_to_png


# Create your views here.
def index(request):
    feed_back = Feedback.objects.order_by('-create_date')
    portfolio = Portfolio.objects.order_by('-create_date')

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

    return render(request, 'main/index.html', {'feed_back': feed_back, 'portfolio': portfolio})


def about(request):
    return render(request, 'main/about.html')


def write(request):
    return render(request, 'main/write.html')


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
