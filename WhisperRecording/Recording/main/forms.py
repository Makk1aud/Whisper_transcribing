from django.forms import ModelForm
from django import forms

class UserInput(forms.Form):
    rec_time = forms.CharField(max_length=100)
    filename = forms.CharField(max_length=100)