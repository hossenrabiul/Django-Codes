from django.urls import path, include
from . import views
urlpatterns = [
   path('add/', views.taskFun, name = 'add_task'),
   path('edit/<int:id>', views.editFun, name = 'edit_task'),
   path('dlt/<int:id>', views.delete_task, name = 'dlt')
]