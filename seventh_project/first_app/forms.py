from django import forms
from first_app.models import Sudentmodel

class StudentForm(forms.ModelForm):
    class Meta:
        model = Sudentmodel
        fields = '__all__'
        labels = {
            'name' : "Student Name",
            'roll' : "Student Roll"
        }
        widgets = {
            'name' : forms.TextInput,
        }
        help_texts = {
            'name' : "write your full name"
        }

        error_messages = {
            'name' : {'required' : "Your name is required"}
        }