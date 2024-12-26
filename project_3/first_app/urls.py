from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home),
    # path('first_app/', include('first_app.urls')),
]