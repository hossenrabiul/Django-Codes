from django.shortcuts import render
from first_app.forms import StudentForm
# Create your views here.

def home(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit = False)
            print(form.cleaned_data)
            
    else:
        form = StudentForm

    return render(request, 'index.html', {'form' : form})
    