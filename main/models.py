from django.db import models
from django.core.exceptions import ValidationError


# Create your models here.
class Feedback(models.Model):
    class Meta:
        verbose_name = 'пользователя с отзывом'
        verbose_name_plural = 'Отзывы'

    name = models.CharField('Имя', max_length=50)
    last_name = models.CharField('Фамилия', max_length=50)
    feedback = models.TextField('Отзыв')
    create_date = models.DateTimeField('Дата отзыва', auto_now_add=True)

    def __str__(self):
        return f'{self.last_name} {self.name}'


class Portfolio(models.Model):
    class Meta:
        verbose_name = 'картинку'
        verbose_name_plural = 'Картинки для портфолио'

    def validate_image_extension(value):
        if not value.name.endswith(
                ('.jpg', '.JPG', '.jpeg', '.JPEG', '.png', '.PNG', '.gif', '.GIF', '.bmp', '.BMP', '.heic', '.HEIC')):
            raise ValidationError(
                'Неподдерживаемое расширение файла. Поддерживаются только изображения в форматах .jpg, .jpeg, .png, '
                '.gif, heic .bmp.')

    img = models.FileField(
        blank=True,
        upload_to='images-slider',
        validators=[validate_image_extension],
        verbose_name='Картинка'
    )
    create_date = models.DateTimeField('Дата публикации', auto_now_add=True)

    def __str__(self):
        return f'Картинка {str(self.create_date)[:10]}'
