from django.db import models
from category.models import TaskCategory

# Create your models here.
class TaskModel(models.Model):
    taskTitle = models.CharField(max_length=50)
    taskDescription = models.TextField()
    is_Completed = models.BooleanField(default=False)
    taskAssignDate = models.DateField()
    cate = models.ManyToManyField(TaskCategory)
    def __str__(self):
        return f'Title : {self.taskTitle}'