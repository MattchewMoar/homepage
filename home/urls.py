from django.urls import path 
from .views import HomeView, ProjectView, ContactView, new_post

urlpatterns = [
    path('home', HomeView.as_view(), name='home'),
    path('', HomeView.as_view(), name='home'),
    path('projects', ProjectView.as_view(), name='projects'),
    path('contact', ContactView.as_view(), name='contact'),
    path('new_post/', new_post, name='new_post'),

]