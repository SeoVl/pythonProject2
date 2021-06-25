from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['model', 'engine', 'speed', 'date']

        widgets = {
            "model": TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Название машины'
            }),
            "engine": TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Двигатель'
            }),
            "speed": TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Разгон(0-100)'
            }),
            "date": DateTimeInput(attrs={
                'class': "form-control",
                'placeholder': 'Дата публикации'
            }),
        }
