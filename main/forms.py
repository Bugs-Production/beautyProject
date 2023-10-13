from .models import Feedback
from price.models import Order, Service, ManicureType
from courses.models import CourseWrite, Course
from django.forms import ModelForm, TextInput, Textarea, Select
from django import forms


class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'last_name', 'feedback']

        widgets = {
            'name': TextInput(attrs={
                'class': 'col-12 col-md-8 mb-3',
                'placeholder': 'Введите имя',
            }),
            'last_name': TextInput(attrs={
                'class': 'col-12 col-md-8 mb-3',
                'placeholder': 'Введите фамилию',
            }),
            'feedback': Textarea(attrs={
                'class': 'col-12 col-md-8',
                'placeholder': 'Оставьте свой отзыв',
            }),
        }


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'last_name', 'phone_number', 'services', 'manicure_types_service1', 'manicure_types_service2',
                  'manicure_types_service3']
        widgets = {
            'name': TextInput(attrs={
                'class': 'col-12 col-md-8 mb-3',
                'placeholder': 'Введите имя',
            }),
            'last_name': TextInput(attrs={
                'class': 'col-12 col-md-8 mb-3',
                'placeholder': 'Введите фамилию',
            }),
            'phone_number': TextInput(attrs={
                'class': 'col-12 col-md-8 mb-3',
                'placeholder': 'Номер телефона',
            }),
        }

    services = forms.ModelMultipleChoiceField(
        queryset=Service.objects.all(),
        required=False,
    )

    manicure_types_service1 = forms.ModelMultipleChoiceField(
        queryset=ManicureType.objects.filter(service__name_service='Маникюр'),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    manicure_types_service2 = forms.ModelMultipleChoiceField(
        queryset=ManicureType.objects.filter(service__name_service='Наращивание'),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    manicure_types_service3 = forms.ModelMultipleChoiceField(
        queryset=ManicureType.objects.filter(service__name_service='Педикюр'),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )


class CourseForm(ModelForm):
    class Meta:
        model = CourseWrite
        fields = ['name', 'last_name', 'phone_number', 'courses']

        widgets = {
            'name': TextInput(attrs={
                'class': 'col-12 col-md-8 mb-3',
                'placeholder': 'Введите имя',
            }),
            'last_name': TextInput(attrs={
                'class': 'col-12 col-md-8 mb-3',
                'placeholder': 'Введите фамилию',
            }),
            'phone_number': TextInput(attrs={
                'class': 'col-12 col-md-8 mb-3',
                'placeholder': 'Номер телефона',
            }),
        }

    courses = forms.ModelChoiceField(
        queryset=Course.objects.all(),
        empty_label="Выберите курс",
        widget=Select(attrs={
            'class': 'col-12 col-md-8 mb-3 form-select-lg',
        })
    )