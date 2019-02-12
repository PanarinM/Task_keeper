from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'tasks'

urlpatterns = [
path('login/',
         auth_views.LoginView.as_view(template_name='accounts/login.html'),
         name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('', views.MainPage.as_view(), name='main'),
    path('add_group/', views.add_group, name='add_group'),
    path('edit_group/<int:id>/', views.edit_group, name='edit_group'),
    path('delete_group/<int:id>/', views.delete_group, name='delete_group'),
    path('board/', views.tasks, name='board'),
    path('details/<int:id>/', views.details, name='details'),
    path('add_task/<int:id>/', views.add_task, name='add_task'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('move/<int:id>/', views.move_to_next, name='move'),
]
