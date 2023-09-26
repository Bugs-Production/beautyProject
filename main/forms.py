from .models import Feedback
from django.forms import ModelForm, TextInput, Textarea


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
                'class': 'col-md-8',
                'placeholder': 'Оставьте свой отзыв',
            }),
        }
