from django import forms

from PIL import Image


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50)
    email = forms.CharField(max_length= 50)
    password = forms.CharField(widget = forms.PasswordInput())
    gender = forms.CharField(max_length=50)
    
    
class LoginForm(forms.Form):
    email = forms.CharField(max_length=50)
    password = forms.CharField(max_length= 50)