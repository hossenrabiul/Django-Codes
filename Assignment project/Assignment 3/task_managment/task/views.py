from django.shortcuts import render, redirect
from . forms import TaskForm
from . import models
# Create your views here.

def taskFun(request):
    if request.method == 'POST':
        task_form = TaskForm(request.POST)
        if task_form.is_valid():
            task_form.save()
            return redirect('home_page')
    else:
        task_form = TaskForm()

    return render(request, 'taskField.html', {'form' : task_form})

def editFun(request, id):
    idd = models.TaskModel.objects.get(pk = id)
    print(idd)
    taskform = TaskForm(instance=idd)
    if request.method == 'POST':
        taskform = TaskForm(request.POST, instance=idd)
        if taskform.is_valid():
            taskform.save()
            return redirect('home_page')
    
    return render(request, 'taskField.html', {'form' : taskform})

def delete_task(request, id):
    dlt = models.TaskModel.objects.get(pk = id)
    dlt.delete()
    return redirect('home_page')
 
    
