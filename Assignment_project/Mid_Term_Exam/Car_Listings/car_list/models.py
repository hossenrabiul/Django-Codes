from django.db import models
from django.contrib.auth.models import User
from car_brand.models import Brand
# Create your models here.

class CarList(models.Model):
    CarName = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    Brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=None)
    image = models.ImageField(upload_to='uploads/', blank = True, null = True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f'Name : {self.CarName}'
    
    
class Comment(models.Model):
    post = models.ForeignKey(CarList, on_delete = models.CASCADE, related_name=  'comments')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comments by : {self.name}"

    