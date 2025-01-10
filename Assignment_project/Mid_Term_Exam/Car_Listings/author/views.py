from django.shortcuts import render, redirect
from . import forms 
from . import models
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from car_list.models import CarList
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
# # Create your views here.
# # Create your views here.


def register(request):
    if request.method == 'POST':

        register_form = forms.Registration(request.POST)
        if register_form.is_valid():
            print(register_form.cleaned_data)
            register_form.save()
            messages.success(request, 'Account Created Successfully')
            return redirect('register')
    else:
        register_form = forms.Registration()
        
    return render(request, 'register_form.html', {'form' : register_form, 'type' : 'Register'})



class UserLoginView(LoginView):
    template_name = 'register_form.html'
    # success_url = reverse_lazy('profile')
    def get_success_url(self):
        return reverse_lazy('profile')


    def form_valid(self, form):
        messages.success(self.request, 'Logged In Successfully ')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.success(self.request, 'Logged In information incorrect ')
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context



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
                return redirect('login')
            else:
                messages.warning(request, 'Login information is not Correct')
                return redirect('login')
    else:
        form = AuthenticationForm(request.user)
        return render(request, 'register_form.html', {'form' : form, 'type' : 'login'})
    


@login_required
def profile(request):  
    data = CarList.objects.filter(author = request.user)
    Transactioon = models.History.objects.filter(author = request.user)
    return render(request, 'profile.html', {'data' : data, 'historys' : Transactioon})


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
        
    return render(request, 'paswrd_chnge.html', {'form' : form})


def user_logout(request):
    logout(request)
    return redirect('login')