from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Post, Bio, ContactInfo


# Create your views here.
#def home(request):
#    return render(request, 'home/home.html', {})
class HomeView(TemplateView):
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bio'] = Bio.objects.all()
        return context



class ProjectView(TemplateView):
    template_name = 'home/projects.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        return context

class ContactView(TemplateView):
    template_name = 'home/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact'] = ContactInfo.objects.all()
        return context

