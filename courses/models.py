from django.db import models
from pytils.translit import slugify

from django.contrib import admin


# Create your models here.
class Course(models.Model):
    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'Курсы'

    name = models.CharField('Наименование курса', max_length=50)
    img = models.ImageField('Картинка для курса', upload_to='img-courses')
    mini_description = models.TextField('Мини описание курса')
    count_group = models.CharField('Количество людей в группе', max_length=30)
    time_course = models.CharField('Длительность курса', max_length=30)
    certificate = models.CharField('Документ об окончании курса', max_length=30)
    price = models.IntegerField('Стоимость курса')
    description = models.TextField('Полное описание курса')
    create_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True, verbose_name='Slug')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Course, self).save(*args, **kwargs)


class CourseWrite(models.Model):
    class Meta:
        verbose_name = 'запись на курс'
        verbose_name_plural = 'Клиенты курса'

    create_date = models.DateTimeField('Дата записи', auto_now_add=True)
    name = models.CharField('Имя', max_length=50, blank=False)
    last_name = models.CharField('Фамилия', max_length=50, blank=False)
    phone_number = models.CharField('Номер телефона', max_length=18, blank=False)
    courses = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_write',
                                verbose_name='Курс')

    def __str__(self):
        return f'{self.last_name} {self.name}'


class CourseWriteAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'last_name',
        'phone_number',
        'courses',
        'create_date',
    )

    list_filter = ('courses',)