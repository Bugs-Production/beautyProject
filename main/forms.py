from .models import Feedback
from price.models import Order
from django.forms import ModelForm, TextInput, Textarea
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
        fields = ['name', 'last_name', 'phone_number', 'services', 'manicure_types']

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
            'manicure_types': forms.CheckboxSelectMultiple(),
            'services': forms.CheckboxSelectMultiple(),
        }
