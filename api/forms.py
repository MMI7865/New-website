from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

class SignUpForm(UserCreationForm):
    profile_pic = forms.ImageField(required=False)
    date_of_birth = forms.DateField(required=False)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'profile_pic', 'date_of_birth')

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')