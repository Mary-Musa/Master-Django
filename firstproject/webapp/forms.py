from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput,TextInput


#register/create user
class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password1','password2']
#login user

class LoginForm(AuthenticationForm):
    
    username=forms.CharField(widget=TextInput())
    password=forms.CharField(widget=PasswordInput())