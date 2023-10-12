from rest_framework import serializers
from price.models import Order, ManicureType, Service


class ManicureTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManicureType
        fields = ('name', 'price')


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('name_service',)


class OrderSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    last_name = serializers.CharField()
    phone_number = serializers.CharField()

    services = ServiceSerializer(many=True)
    manicure_types_service1 = ManicureTypeSerializer(many=True)
    manicure_types_service2 = ManicureTypeSerializer(many=True)
    manicure_types_service3 = ManicureTypeSerializer(many=True)

    class Meta:
        model = Order
        fields = '__all__'
