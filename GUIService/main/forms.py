from django import forms
from django.forms import ClearableFileInput
from .models import Person, PersonImages, PersonA


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name']


class PersonImageForm(forms.ModelForm):
    class Meta:
        model = PersonImages
        fields = ['images']
        widgets = {
            'images': ClearableFileInput(attrs={'multiple': True}),
        }

class PersonAForm(forms.ModelForm):
    class Meta:
        model = PersonA
        fields = ('name', 'images')
        widgets = {
            'images': ClearableFileInput(attrs={'multiple': True}),
        }