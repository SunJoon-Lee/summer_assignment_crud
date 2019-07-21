from django import forms
from .models import Appcrud, Comment

class AppcrudForm(forms.ModelForm):
    class Meta:
        model = Appcrud
        fields = ['title', 'body']

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)