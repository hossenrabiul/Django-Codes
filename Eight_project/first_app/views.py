from django.shortcuts import render, redirect
from .forms import ReginterForm, changeUserData
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
# Create your views here.

def home(request):
    return render(request, 'home.html')

def signUp(request):
    if not request.user.is_authenticated:

        if request.method == 'POST':
            form = ReginterForm(request.POST)
            if form.is_valid():
                messages.success(request, 'Account created successfully')
                # messages.warning(request, 'warning')
                # messages.info(request, 'info')
                form.save()
                print(form.cleaned_data)
        else:
            form = ReginterForm()
        return render(request, './sign_up.html', {'form' : form})
    
    else:
        return redirect('login')

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request = request, data = request.POST)
            if form.is_valid():
                name = form.cleaned_data['username']
                userpass = form.cleaned_data['password']
                user = authenticate(username = name, password = userpass) # check krteci useer database ee ace kina
                if user is not None:
                    login(request, user)
                    return redirect('profile')    #
        else:
            form = AuthenticationForm()

        return render(request, './login.html', {'form' : form})
    else:
        return redirect('profile')
    
    
def profile(request):

    if request.user.is_authenticated:

        if request.method == 'POST':
            form = changeUserData(request.POST, instance = request.user)
            if form.is_valid():
                messages.success(request, 'Account updated successfully')
                form.save()
                print(form.cleaned_data)
        else:
            form = changeUserData(instance = request.user)
        return render(request, './profile.html', {'form' : form})
    
    else:
        return redirect('signup')




    # if request.user.is_authenticated:
    #     return render(request, './profile.html', {'user' : request.user})
    # else:
    #     return redirect('login')

def user_logout(request):
    logout(request)
    return redirect('login')
 

def pass_change(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(user=request.user, data = request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user) # password update krbe
                return redirect('login')
            
        else:
            form = PasswordChangeForm(user = request.user)

        return render(request, './passchange.html', {'form' : form})
    else:
        return redirect('signup')


# change password without old password
def pass_change2(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SetPasswordForm(user=request.user, data = request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user) # password update krbe
                return redirect('login')
            
        else:
            form = SetPasswordForm(user = request.user)

        return render(request, './passchange.html', {'form' : form})
    else:
        return redirect('signup')


# def changeUserData(request):
#     if request.user.is_authenticated:

#         if request.method == 'POST':
#             form = changeUserData(request.POST, isinstance = request.user)
#             if form.is_valid():
#                 messages.success(request, 'Account updated successfully')
#                 # messages.warning(request, 'warning')
#                 # messages.info(request, 'info')
#                 form.save()
#                 print(form.cleaned_data)
#         else:
#             form = changeUserData()
#         return render(request, './profile.html', {'form' : form})
    
#     else:
#         return redirect('signup')