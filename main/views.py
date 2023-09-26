from django.shortcuts import render
from .models import Feedback


# Create your views here.
def index(request):
    feed_back = Feedback.objects.order_by('-create_date')
    return render(request, 'main/index.html', {'feed_back': feed_back})


def about(request):
    return render(request, 'main/about.html')


def write(request):
    return render(request, 'main/write.html')


def feedback(request):
    return render(request, 'main/feedback.html')
