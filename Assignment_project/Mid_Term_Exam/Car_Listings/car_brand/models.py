from django.db import models

# Create your models here.

class Brand(models.Model):
    BrandName = models.CharField(max_length=100)