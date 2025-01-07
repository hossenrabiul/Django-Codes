from django.urls import path
from . import views
urlpatterns = [
   
    path('add/', views.addBrandName, name = 'add_brand'),
]