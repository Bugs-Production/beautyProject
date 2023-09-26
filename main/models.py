from django.db import models


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
