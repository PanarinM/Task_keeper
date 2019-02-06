from django.contrib import admin
from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.MainPage.as_view(), name='main'),
    path('board/', views.tasks, name='board'),
    path('details/<int:id>/', views.details, name='details'),
    path('add_task/', views.add_task, name='add_task'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('move/progress/<int:id>/', views.move_to_progress, name='progress'),
    path('move/done/<int:id>/', views.move_to_done, name='done')
]