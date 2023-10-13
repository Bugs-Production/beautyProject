from django.urls import path

from .views import index, about, write, feedback, thanks, write_confirmed, CoursesView, CourseView, write_course, \
    course_confirmed

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('record/', write, name='record'),
    path('record/confirmed', write_confirmed, name='confirmed'),
    path('feedback/', feedback, name='feedback'),
    path('feedback/thanks', thanks, name='thanks'),
    path('courses', CoursesView.as_view(), name='courses'),
    path('courses/confirmed', course_confirmed, name='course-confirmed'),
    path('courses/<slug:slug>', CourseView.as_view(), name='course'),
    path('courses/<slug:course_slug>/enroll/', write_course, name='enroll-course'),
]
