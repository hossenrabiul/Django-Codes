from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home),
    path('about/', views.about, name = 'about_page'),
    path('form/', views.submit_form, name = 'submit_form'),
    path('django_/', views.DjangoForm, name = 'django_form'),
    # path('student/', views.student, name = 'student_form')
    path('password', views.password_check, name = 'student_form')

 
]