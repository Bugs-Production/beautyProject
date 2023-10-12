from django.urls import path
from .views import ApiOrder

urlpatterns = [
    path('', ApiOrder.as_view()),
]
