from django import forms
from .models import CarList, Comment

class CarForm(forms.ModelForm):
    class Meta:
        model = CarList
        fields = '__all__'

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']
       