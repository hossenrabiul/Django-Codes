from django.urls import path, include
from . import views
urlpatterns = [
    path('addCar/', views.add_carList, name = "addCar"),
    path('edit/<int:id>/', views.EditPostView.as_view(), name = 'edit_post'),
    path('delete/<int:id>/', views.DeletePostView.as_view(), name = 'delete_post'),
    path('details/<int:id>/', views.detail, name = 'detail_post'),
    path('buy/<int:id>/', views.BuyProduct, name = 'buy'),

]