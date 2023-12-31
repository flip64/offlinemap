from django import forms
from django.forms import ModelForm
class FilesForm(forms.Form):
    file = forms.FileField()
    
    