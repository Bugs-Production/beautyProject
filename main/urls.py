from django.urls import path

from .views import index, about, write, feedback

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('record/', write, name='record'),
    path('feedback/', feedback, name='feedback'),
]
