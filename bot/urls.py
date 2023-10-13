from django.urls import path
from .views import ApiOrder, ApiCourse

urlpatterns = [
    path('', ApiOrder.as_view()),
    path('course', ApiCourse.as_view()),
]
