from django import forms
from .models import search

class SerchForm(forms.ModelForm):
    class Meta:
        model=search
        fields = ['address',]

