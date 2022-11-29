from django.urls import path 
from .views import HomeView, ProjectView, ContactView

urlpatterns = [
    path('home', HomeView.as_view(), name='home'),
    path('', HomeView.as_view(), name='home'),
    path('projects', ProjectView.as_view(), name='projects'),
    path('contact', ContactView.as_view(), name='contact'),

]