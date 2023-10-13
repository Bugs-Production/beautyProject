from django.contrib import admin
from .models import Course, CourseWrite, CourseWriteAdmin

# Register your models here.
admin.site.register(Course)
admin.site.register(CourseWrite, CourseWriteAdmin)
