from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=20)
    roll = models.IntegerField(primary_key=True)
    address = models.TextField()
    field = models.TextField(default='rahim')

    def __str__(self):
        return f"roll : {self.roll} - name : {self.name}"