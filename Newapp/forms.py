from django import forms
from django.contrib.auth.forms import UserCreationForm

from Newapp.models import Login, studentreg


class Loginregister(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label="password",widget=forms.PasswordInput)
    password2 = forms.CharField(label="confirm password",widget=forms.PasswordInput)

    class Meta:
        model = Login
        fields = ("username","password1","password2")



class studentregform(forms.ModelForm):
    class Meta:
        model = studentreg
        fields = ("name","phone","email","rollnumber","collegename")