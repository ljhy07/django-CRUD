from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('', views.view.home, name='home'),
    
    path('create', views.view.create_student, name='create_student'),
    path('read', views.view.read_student, name='read_student'),
    path('update', views.view.update_student, name='update_student'),
    path('delete', views.view.delete_student, name='delete_student'),

    path('input_delete', views.view.input_delete, name='input_delete'),
    path('input_update', views.view.input_update, name='input_update'),
    path('input_read', views.view.input_read, name='input_read')
]