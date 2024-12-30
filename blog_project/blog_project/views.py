from django.shortcuts import render
from posts.models import Post
def home(request):
    data = Post.objects.all()
    print(data)
    # for i in data:
    #     print(i.title)
    #     for j in i.category:
    #         print(j)
    return render(request, 'index.html', {'data' : data})