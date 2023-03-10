from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    email = forms.EmailField(label="E-mail")
    age = forms.IntegerField(label="Age")
    class Meta:
        model = User
        fields = ("username", "password1", "password2", "email", "age")