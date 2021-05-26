from .models import Art
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, DateInput, TimeInput, IntegerField
from django import forms

class ArticlesForm(ModelForm):
    class DateInput(forms.DateInput):
        input_type = 'date'

    class Meta:
        model = Art
        fields = ["title", 'anon', 'full', 'date', 'vdate', 'vtime', 'vgost']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название статьи'
            }),
            "anon": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Анонс статьи'
            }),
            "date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата',
                'type': 'datetime'
            }),
            "full": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст'
            }),
            "vdate": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата',
                'type': 'date'
            }),
            "vtime": TimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Время',
                'type': 'time'
            }),
            # "vgost": IntegerField(attrs={
            #     'class': 'form-control',
            #     'placeholder': 'Дата'
            # }),
        }