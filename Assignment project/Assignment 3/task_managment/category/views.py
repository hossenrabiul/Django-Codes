from django.shortcuts import render,redirect
from . forms import categoryForm
# Create your views here.

def categoryFun(request):
    if request.method == 'POST':
        cat_form = categoryForm(request.POST)
        if cat_form.is_valid():
            cat_form.save()
            return redirect('home_page')
    else:
        cat_form = categoryForm()
        
    return render(request, 'categoryField.html', {'form' : cat_form})