from django.shortcuts import render
from car_list.models import CarList
def home(request):
    data = CarList.objects.all()
    return render(request, 'home.html', {'data' : data})