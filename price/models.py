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
        return f'{self.name}'


class ManicureTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'service', 'price')
    list_filter = ('service__name_service',)


class Order(models.Model):
    class Meta:
        verbose_name = 'запись'
        verbose_name_plural = 'Записи'

    create_date = models.DateTimeField('Дата записи', auto_now_add=True)
    name = models.CharField('Имя', max_length=50, blank=False)
    last_name = models.CharField('Фамилия', max_length=50, blank=False)
    phone_number = models.CharField('Номер телефона', max_length=15, blank=False)
    services = models.ManyToManyField(Service, verbose_name='Вид услуги')
    manicure_types = models.ManyToManyField(ManicureType, verbose_name='Виды маникюра', blank=True)

    def str(self):
        return f'{self.name} {self.last_name}'


class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'last_name',
        'phone_number',
        'display_manicure_types',
        'total_price',
        'create_date'
    )
    list_filter = ('services',)

    def display_manicure_types(self, obj):
        # Получить выбранные виды маникюра для данного заказа
        manicure_types = obj.manicure_types.all()

        # Преобразовать их в строку, разделенную запятыми, и вернуть
        return ', '.join(str(man) for man in manicure_types)

    display_manicure_types.short_description = 'Виды маникюра'

    def total_price(self, obj):
        # Получить выбранные виды маникюра для данного заказа
        manicure_types = obj.manicure_types.all()

        # Посчитать общую сумму цен на выбранные виды маникюра
        total = sum(man.price for man in manicure_types)

        return total

    total_price.short_description = 'Общая сумма'
