from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class meta:
        model = User
        fields = ['usrname' , 'email','password1','password2']


class UserUpadateForm(forms.ModelForm):
    email = forms.EmailField()

    class meta:
        model = User
        fields = ['usrname' , 'email']

class ProfileUpadteForm(forms.ModelForm):
    class meta:
        model = Profile
        fields = ['image']
