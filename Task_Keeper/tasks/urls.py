from django.contrib import admin
from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.MainPage.as_view(), name='main'),
    path('add_group/', views.add_group, name='add_group'),
    path('delete_group/<int:id>/', views.delete_group, name='delete_group'),
    path('board/', views.tasks, name='board'),
    path('details/<int:id>/', views.details, name='details'),
    path('add_task/<int:id>/', views.add_task, name='add_task'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('move/<int:id>/', views.move_to_next, name='move'),
]