from django.contrib import admin
from .models import Feedback, Portfolio

# Register your models here.
admin.site.register(Feedback)
admin.site.register(Portfolio)
admin.site.site_header = 'Админ-панель мастера Валерии'
