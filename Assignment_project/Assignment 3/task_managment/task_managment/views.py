from django.shortcuts import render
from task.models import TaskModel
def home(request):
    showTask = TaskModel.objects.all()
    print(showTask)
    return render(request, 'home.html', {'form' : showTask})