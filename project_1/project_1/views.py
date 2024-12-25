from django.http import HttpResponse


def home(request):
    return HttpResponse('This is a home page')
def contact(request):
    return HttpResponse('This is a contact page')