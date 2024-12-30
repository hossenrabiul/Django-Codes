from django import forms
from django.core import validators

class contactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    file = forms.FileField()
    CHOICES = [('S', 'Small'), ('M', 'Medium'), ('L', 'Large')]
    size = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    MEAL = [('B', 'Brukholi', ('T', 'Tomato'), ('L', 'Letus'))]
    pizza = forms.MultipleChoiceField(choices=MEAL, widget=forms.CheckboxSelectMultiple)
    # age = forms.CharField(widget=forms.NumberInput)
    birthday = forms.CharField(widget=forms.DateInput(attrs={'type' : 'date'}))
    appoinment = forms.CharField(widget=forms.DateInput(attrs={'type' : 'datetime_local'}))



# class studentData(forms.Form):
#     name = forms.CharField(widget=forms.TextInput)
#     email = forms.CharField(widget=forms.EmailInput)
    # def clean_name(self):
    #     valName = self.cleaned_data['name']
    #     if len(valName) <10:
    #         raise forms.ValidationError("Enter a name with at least 10 characters")
    #     else:
    #         return valName 


    # excess all the value of this funtion studentData at once
    # def clean(self):
    #     cleaned_data = super().clean()

    #     valname = self.cleaned_data['name']
    #     valemail = self.cleaned_data['email']
    #     if len(valname) < 10:
    #         raise forms.ValidationError("Enter a name with atleast 10 character")
        
    #     if '.com' not in valemail:
    #         raise forms.ValidationError("Your email must contain .com ")


class studentData(forms.Form):
    name = forms.CharField(widget=forms.TextInput, validators=[validators.MinLengthValidator(10, message="Your name must contains 10 character")])

    email = forms.CharField(widget=forms.EmailInput, validators=[validators.EmailValidator(message="Enter a valid email")])

    age = forms.IntegerField(validators=[validators.MinValueValidator(24, message="age must be at least 24"), validators.MaxValueValidator(34, message="age must be maximum 34")])

    file = forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf'], message="file extention allow pdf only")])


class passwordValidationProject(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    password =forms.CharField(widget=forms.PasswordInput)
    comfirm_password =forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        valPass = self.cleaned_data['password']
        valCom_Pass = self.cleaned_data['comfirm_password']

        if valPass != valCom_Pass:
            raise forms.ValidationError("password does not match")