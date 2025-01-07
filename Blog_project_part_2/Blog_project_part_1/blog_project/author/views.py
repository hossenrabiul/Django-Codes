from django.shortcuts import render, redirect
from . import forms 
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from posts.models import Post
# Create your views here.


# def add_author(request):
#     if request.method == 'POST':

#         author_form = forms.AuthorForm(request.POST)
#         if author_form.is_valid():
#             print(author_form.cleaned_data)
#             author_form.save()
#             return redirect('add_author')
#     else:
#         author_form = forms.AuthorForm()
        
#     return render(request, 'add_author.html', {'form' : author_form})


def register(request):
    if request.method == 'POST':

        register_form = forms.Registration(request.POST)
        if register_form.is_valid():
            print(register_form.cleaned_data)
            register_form.save()
            messages.success(request, 'Account Created Successfully')
            return redirect('profile')
    else:
        register_form = forms.Registration()
        
    return render(request, 'register_form.html', {'form' : register_form, 'type' : 'Register'})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.user, data = request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            user_pass = form.cleaned_data['password']
            user = authenticate(username = user_name, password = user_pass)
            if user is not None:
                login(request, user)
                messages.success(request, 'Logged in Successfully')
                return redirect('profile')
            else:
                messages.warning(request, 'Login information is not Correct')
                return redirect('login')
    else:
        form = AuthenticationForm(request.user)
        return render(request, 'register_form.html', {'form' : form, 'type' : 'login'})
    

@login_required
def profile(request):  
    data = Post.objects.filter(author = request.user)
    return render(request, 'profile.html', {'data' : data})


@login_required
def edit_profile(request):

    if request.method == 'POST':

        profile_form = forms.changeUserForm(request.POST, instance = request.user)
        if profile_form.is_valid():
            print(profile_form.cleaned_data)
            profile_form.save()
            messages.success(request, 'Profile Updated Successfully')
            return redirect('profile')
    else:
        profile_form = forms.changeUserForm(instance = request.user)
        
    return render(request, 'update_profile.html', {'form' : profile_form})


def change_pass(request):
    if request.method == 'POST':

        form =  PasswordChangeForm(request.user, data = request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            messages.success(request, 'Password Updated Successfully')
            update_session_auth_hash(request, form.user)
            return redirect('profile')
    else:
        form =  PasswordChangeForm(request.user)
        
    return render(request, 'pass_change.html', {'form' : form})

def user_logout(request):
    logout(request)
    return redirect('login')