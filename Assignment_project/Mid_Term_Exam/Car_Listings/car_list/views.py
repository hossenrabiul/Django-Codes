from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from . import models
from author.models import History
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView, DeleteView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
# Create your views here.

 
class CarView(LoginRequiredMixin,CreateView):
    template_name = 'add_car_list.html'
    form_class = forms.CarForm
    model = models.CarList 
    success_url = reverse_lazy('home_page')
    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request,"Added successfull")
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.error(self.request,"invalid info")
        return super().form_invalid(form)



@login_required
def add_carList(request):
    if request.method == 'POST':
        car_form = forms.CarForm(request.POST)
        if car_form.is_valid():
            car_form.instance.author = request.user
            car_form.save()
            return redirect('addCar')
    else:
        car_form = forms.CarForm()

    return render(request, 'add_car_list.html',{'form' : car_form})


@method_decorator(login_required, name = 'dispatch')
class EditPostView(UpdateView):
    model = models.CarList
    form_class = forms.CarForm
    template_name = 'add_car_list.html'
    success_url = reverse_lazy('home_page')
    pk_url_kwarg = 'id'
 

@method_decorator(login_required, name = 'dispatch')
class DeletePostView(DeleteView):
    model = models.CarList
    template_name = 'delete.html'
    success_url = reverse_lazy('profile')
    pk_url_kwarg = 'id'


def detail(request, id):
    model = models.CarList.objects.get(pk = id)
    print(model)
    comments = models.Comment.objects.filter(post = model )

    if request.method == 'POST':
        comment_form = forms.CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = model 
            comment.save()
            return redirect('detail_post', id = id)
    else:
        comment_form = forms.CommentForm()
    return render(request, 'post_details.html', {'post' : model, 'comments' : comments, 'comment_form' : comment_form})




def BuyProduct(request, id=None):
    if id:
        car = models.CarList.objects.get(pk=id) 
        user = request.user
        history = user.history

        print(user.username) 
        if car.quantity > 0:
            car.quantity -= 1
            car.save()  
            History.objects.create(
                title=f"Purchased {car.CarName}",
                money=car.price,  
                author=user  
            )
            messages.success(request, 'Congratulation! Best of luck!') 

        else:
            messages.error(request,'Unabilable Cars')
        return redirect('detail_post', id=id)
    else:
        return redirect('home_page')

