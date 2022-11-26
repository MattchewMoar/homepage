from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.home, name='home.html'),
    path('projects/', views.projects, name='projects.html'),

]