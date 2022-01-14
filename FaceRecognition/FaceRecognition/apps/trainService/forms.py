from .models import UserRecognizer
from django.forms import ModelForm, TextInput, PasswordInput

class UserRecognizerForm(ModelForm):
    class Meta:
        model = UserRecognizer
        fields = ['login', 'password']

        widgets = {
            'login': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Recognizer name'
            }),
            "password": PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Password'
            })
        }