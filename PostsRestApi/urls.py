from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home),
    path('create_post/', views.create_post),
    path('delete_post/', views.delete_post),
    path('api-auth/', include('rest_framework.urls',
         namespace='rest_framework'))
]