from django.db import models
# from task.models import TaskModel
# Create your models here.

class TaskCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'name : {self.name}'


