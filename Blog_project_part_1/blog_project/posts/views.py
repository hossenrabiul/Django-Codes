from django.shortcuts import render, redirect
from . import forms
from . import models
# Create your views here.

def add_post(request):
    if request.method == 'POST':
        post_form = forms.postForm(request.POST)
        if post_form.is_valid():
            post_form.save()
            return redirect('add_posts')
    else:
        post_form = forms.postForm()

    return render(request, 'add_post.html',{'form' : post_form})


def edit_post(request, id):
    post = models.Post.objects.get(pk = id)
    post_form = forms.postForm(instance=post)
    print(post.title)
    if request.method == 'POST':
        post_form = forms.postForm(request.POST, instance=post)
        if post_form.is_valid():
            post_form.save()
            return redirect('home_page')
        
    return render(request, 'add_post.html',{'form' : post_form})

def delete_post(request, id):
    post = models.Post.objects.get(pk = id)
    post.delete()
    return redirect('home_page')