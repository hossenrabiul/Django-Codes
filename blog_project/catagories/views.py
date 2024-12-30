from django.shortcuts import render, redirect
from . import forms
# Create your views here.

def add_category(request):
    if request.method == 'POST':
        category_form = forms.category_Form(request.POST)
        if category_form.is_valid():
            category_form.save()
            return redirect('add_catagories')
    else:
        category_form = forms.category_Form()
    return render(request, 'add_catagories.html',{'form' : category_form})