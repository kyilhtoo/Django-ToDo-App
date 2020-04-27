from django.urls import path
from . import views

urlpatterns = [
    path('', views.TasksList.as_view(), name='list_task'),
    path('add/', views.addTask, name='create_task'),
    path('<int:pk>/delete/', views.deleteTask, name='delete_task'),
]