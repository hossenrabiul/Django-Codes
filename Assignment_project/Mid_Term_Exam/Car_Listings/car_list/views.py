from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def add_carList(request):
    if request.method == 'POST':
        car_form = forms.CarForm(request.POST)
        if car_form.is_valid():
            # post_form.cleaned_data['author'] = request.user
            # car_form.instance.author = request.user
            car_form.save()
            return redirect('addCar')
    else:
        car_form = forms.CarForm()

    return render(request, 'add_car_list.html',{'form' : car_form})