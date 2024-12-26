from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, ('index.html'))


def submit_form(request):
    return render(request, ('from.html'))