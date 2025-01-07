from django.urls import path, include
from . import views
urlpatterns = [
    path('addCar/', views.add_carList, name = "addCar")

]