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
    services = models.ManyToManyField(Service, verbose_name='Вид услуги', blank=True)
    manicure_types_service1 = models.ManyToManyField(
        ManicureType,
        verbose_name='Маникюр',
        blank=True,
        related_name='orders_service1',
        limit_choices_to={'service__name_service': 'Маникюр'}
    )

    manicure_types_service2 = models.ManyToManyField(
        ManicureType,
        verbose_name='Наращивание',
        blank=True,
        related_name='orders_service2',
        limit_choices_to={'service__name_service': 'Наращивание'}
    )

    manicure_types_service3 = models.ManyToManyField(
        ManicureType,
        verbose_name='Педикюр',
        blank=True,
        related_name='orders_service3',
        limit_choices_to={'service__name_service': 'Педикюр'}
    )

    def __str__(self):
        return f'{self.name} {self.last_name}'


class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'last_name',
        'phone_number',
        'display_manicure_types',
        'total_cost',
        'create_date'
    )

    def display_manicure_types(self, obj):
        return ", ".join([str(man) for man in obj.manicure_types_service1.all()] +
                         [str(man) for man in obj.manicure_types_service2.all()] +
                         [str(man) for man in obj.manicure_types_service3.all()])

    display_manicure_types.short_description = 'Виды маникюра'

    def total_cost(self, obj):
        total = 0
        for manicure_type in obj.manicure_types_service1.all():
            total += manicure_type.price
        for manicure_type in obj.manicure_types_service2.all():
            total += manicure_type.price
        for manicure_type in obj.manicure_types_service3.all():
            total += manicure_type.price
        return total

    total_cost.short_description = 'Сумма записи'
