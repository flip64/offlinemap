from django import forms

class FilesForm(forms.Form):
    file = forms.FileField()
    
    