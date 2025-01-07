from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from . import forms
from . import models
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
# Create your views here.

@login_required
def add_post(request):
    if request.method == 'POST':
        post_form = forms.postForm(request.POST)
        if post_form.is_valid():
            # post_form.cleaned_data['author'] = request.user
            post_form.instance.author = request.user
            post_form.save()
            return redirect('add_posts')
    else:
        post_form = forms.postForm()

    return render(request, 'add_post.html',{'form' : post_form})


# Add post usnig class Based view
@method_decorator(login_required, name = 'dispatch')
class AddPostCreateView(CreateView):
    model = models.Post
    form_class = forms.postForm
    template_name = 'add_post.html'
    success_url = reverse_lazy('add_posts')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
   
    

@login_required
def edit_post(request, id):
    post = models.Post.objects.get(pk = id)
    post_form = forms.postForm(instance=post)
    print(post.title)
    if request.method == 'POST':
        post_form = forms.postForm(request.POST, instance=post)
        if post_form.is_valid():
            post_form.instance.author = request.user
            post_form.save()
            return redirect('home_page')
        
    return render(request, 'add_post.html',{'form' : post_form})



@method_decorator(login_required, name = 'dispatch')
class EditPostView(UpdateView):
    model = models.Post
    form_class = forms.postForm
    template_name = 'add_post.html'
    success_url = reverse_lazy('home_page')
    pk_url_kwarg = 'id'



@login_required
def delete_post(request, id):
    post = models.Post.objects.get(pk = id)
    post.delete()
    return redirect('home_page')


@method_decorator(login_required, name = 'dispatch')
class DeletePostView(DeleteView):
    model = models.Post
    template_name = 'delete.html'
    success_url = reverse_lazy('profile')
    pk_url_kwarg = 'id'


def detail(request, id):
    model = models.Post.objects.get(pk = id)
    print(model)
    comment = models.Comment.objects.all()

    if request.method == 'POST':
        comment_form = forms.CommentForm(request.POST)
        if comment_form.is_valid():
            comment_form.instance.author = request.user
        #     comment_form.save()
        #     return redirect('detail_post')
    else:
        comment_form = forms.CommentForm()
    return render(request, 'post_details.html', {'post' : model, 'comments' : comment, 'comment_form' : comment_form})



    
        

   




class DetailPostView(DetailView):
    model = models.Post
    template_name = 'post_details.html'
    pk_url_kwarg = 'id'

    def post(self, request, *args, **kwargs):
        comment_form = forms.CommentForm(data = self.request.POST)
        post = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()

        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object # post model er object ekahane store korlam
        comments = post.comments.all()
        comment_form = forms.CommentForm()

        context['comments'] = comments
        context['comment_form'] = comment_form
        return context