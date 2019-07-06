from django import forms
from .models import Appcrud

class AppcrudForm(forms.ModelForm):
    class Meta:
        model = Appcrud
        fields = ['title', 'body']