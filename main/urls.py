from django.urls import path

from .views import index, about, write, feedback, thanks, write_confirmed

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('record/', write, name='record'),
    path('record/confirmed', write_confirmed, name='confirmed'),
    path('feedback/', feedback, name='feedback'),
    path('feedback/thanks', thanks, name='thanks'),
]
