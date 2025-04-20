from django import forms
from .models import Contactmodel


class Contact(forms.ModelForm):
    class Meta:
        model=Contactmodel
        fields=['firstname','lastname','email','phone','message']