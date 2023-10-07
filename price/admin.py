from django.contrib import admin
from .models import Service, ManicureType, ManicureTypeAdmin, Order, OrderAdmin

# Register your models here.
admin.site.register(Service)
admin.site.register(ManicureType, ManicureTypeAdmin)
admin.site.register(Order, OrderAdmin)
