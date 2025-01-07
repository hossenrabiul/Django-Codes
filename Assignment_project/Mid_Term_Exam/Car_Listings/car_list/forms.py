from django import forms
from .models import CarList

class CarForm(forms.ModelForm):
    class Meta:
        model = CarList
        fields = '__all__'