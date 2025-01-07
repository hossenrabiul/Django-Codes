from django import forms
from . models import Category

class category_Form(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'