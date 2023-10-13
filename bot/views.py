from price.models import Order
from courses.models import CourseWrite
from rest_framework import generics
from .serializers import OrderSerializer, CourseWriteSerializer


# Create your views here.
class ApiOrder(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class ApiCourse(generics.ListAPIView):
    queryset = CourseWrite.objects.all()
    serializer_class = CourseWriteSerializer
