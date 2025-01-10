from django.shortcuts import render
from car_list.models import CarList
from car_brand.models import Brand
def home(request, brand_slug = None):
    data = CarList.objects.all()
    print(data)
    if brand_slug is not None:
        brand = Brand.objects.get(slug = brand_slug)
        data = CarList.objects.filter(Brand = brand)

    brand_name = Brand.objects.all()
    return render(request, 'home.html', {'data' : data, 'brand' : brand_name})