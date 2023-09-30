from django.db import models

from django.contrib import admin


# Create your models here.
class Service(models.Model):
    class Meta:
        verbose_name = 'услугу'
        verbose_name_plural = 'Услуги'

    name_service = models.CharField('Наименование услуги', max_length=50)
    img = models.ImageField('Картинка для услуги', upload_to='img-price')

    def __str__(self):
        return self.name_service


class ManicureType(models.Model):
    class Meta:
        verbose_name = 'маникюр'
        verbose_name_plural = 'Виды маникюра'

    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='manicure_types',
                                verbose_name='Услуга')
    name = models.CharField('Вид маникюра', max_length=50)
    price = models.IntegerField('Цена')

    def __str__(self):
        return f'{self.name} | {self.service}'


class ManicureTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'service', 'price')
    list_filter = ('service__name_service',)
