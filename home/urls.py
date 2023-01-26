from django.urls import path 
from .views import HomeView, ProjectView, ContactView, new_post

urlpatterns = [
    path('home', HomeView.as_view(), name='home'),
    path('', HomeView.as_view(), name='home'),
    path('fakenews', ProjectView.as_view(), name='fakenews'),
    path('contact', ContactView.as_view(), name='contact'),
    path('new_post/', new_post, name='new_post'),

]