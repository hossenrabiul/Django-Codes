from django.urls import path, include
from . import views
urlpatterns = [
 
    path('add/', views.categoryFun, name = "add_category"),

]