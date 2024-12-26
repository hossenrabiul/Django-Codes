from django.shortcuts import render

# Create your views here.

def home(request):
    d = {'author': 'rohim', 'age' : 19, 'lst' : [1, 2, 3, 4], 'courses' : [
        {
            'id' : 1,
            'name' : 'python',
            'fee' : 5000
        },
        {
            'id' : 2,
            'name' : 'django',
            'fee' : 10000
        },
        {
            'id' : 3,
            'name' : 'c',
            'fee' : 1000
        }
    ]}
    return render(request, 'home.html', d)
