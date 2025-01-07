from django.db import models
from django.contrib.auth.models import User
from car_brand.models import Brand
# Create your models here.

class CarList(models.Model):
    brandName = models.CharField(max_length=100)
    # Brand = models.ManyToManyField(Brand, default=None)
    image = models.ImageField(upload_to='uploads/', blank = True, null = True)
    price = models.TextField()

    