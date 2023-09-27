from django.shortcuts import render, redirect
from .models import Feedback, Portfolio
from .forms import FeedbackForm


# Create your views here.
def index(request):
    feed_back = Feedback.objects.order_by('-create_date')
    portfolio = Portfolio.objects.order_by('-create_date')

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
