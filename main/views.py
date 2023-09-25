from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def write(request):
    return render(request, 'main/write.html')


def feedback(request):
    return render(request, 'main/feedback.html')
