from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from . import forms

# Create your views here.

def addBrandName(request):
    if request.method == 'POST':
        brand_form = forms.BrandForm(request.POST)
        if brand_form.is_valid():
            brand_form.save()
            return redirect('add_brand')
    else:
        brand_form = forms.BrandForm()
    return render(request, 'add_brand.html',{'form' : brand_form})


