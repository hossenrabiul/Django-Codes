from django.shortcuts import render

# Create your views here.

def fun(request):
    d = {'id' : 1, 'name' : 'c++', 'marks' : 50, 'lst' : ['py', 'th', 'on'], 'val' : 3,
        'str' : 'chittagong.com', 'nmb' : ['one', 'two', 'three']}
    return render(request, 'first_app\home.html', d)
