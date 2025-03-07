"""
URL configuration for Car_Listings project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name = 'home_page'),
    path('brand/<slug:brand_slug>/', views.home, name = 'brand_wise'),
    path('car/', include('car_feature.urls')),
    path('author/', include('author.urls')),
    path('list/', include('car_list.urls')),
    path('brand/', include('car_brand.urls')),
]

urlpatterns += static(settings.MEDIA_URL, 
                      document_root = settings.MEDIA_ROOT)