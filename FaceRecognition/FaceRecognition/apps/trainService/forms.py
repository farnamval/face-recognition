import hashlib

from .models import UserRecognizer
from django.forms import ModelForm, TextInput, PasswordInput
import bcrypt

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

    def clean_password(self):
        data = self.cleaned_data['password']
        return hashlib.sha1(data.encode('utf-8')).hexdigest()


