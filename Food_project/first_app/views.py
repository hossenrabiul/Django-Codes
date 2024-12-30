from django.shortcuts import render
from . forms import contactForm, studentData, passwordValidationProject
# Create your views here.

def home(request):
    return render(request, ('home.html'))

def submit_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        select = request.POST.get('select')
        return render(request, 'form.html', {'name' : name, 'email' : email, 'select' : select})
    else:
        return render(request, 'form.html')
    # return render(request, ('form.html'))

def about(request):
    # if request.method == 'POST':
    #     name = request.POST.get('username')
    #     email = request.POST.get('email')
    #     return render(request, 'about.html', {'name' : name, 'email' : email})
    # else:
    return render(request, 'about.html')

def DjangoForm(request):
    if request.method == 'POST':
        
        form = contactForm(request.POST, request.FILES)   # WE ARE STORING DATA BY REQUEST.POST WHICH USER GIVEN 
        if form.is_valid():
            
            file = form.cleaned_data['file']
            with open ('./first_app/upload/' + file.name, 'wb+') as destination:
                for chunck in file.chunks():
                    destination.write(chunck)


            print(form.cleaned_data)
            return render(request, 'django_form.html', {'form' : form})
    else:
        form = contactForm()

    return render(request, 'django_form.html', {'form' : form})

def student(request):
    if request.method == 'POST':
        form = studentData(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = studentData()
        
    return render(request, 'student.html', {'form' : form})

def password_check(request):

    if request.method == 'POST':
        form = passwordValidationProject(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = passwordValidationProject()

    return render(request, 'student.html', {'form' : form})




