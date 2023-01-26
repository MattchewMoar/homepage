from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from .models import Post, Bio, ContactInfo
import openai
import os
import datetime
import time

# Create your views here.
#def home(request):
#    return render(request, 'home/home.html', {})
class HomeView(TemplateView):
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bio'] = Bio.objects.get(id=1)
        return context



class ProjectView(TemplateView):
    template_name = 'home/fakenews.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        return context

class ContactView(TemplateView):
    template_name = 'home/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact'] = ContactInfo.objects.get(id=1)
        return context

def new_post1(request):
    if request.method == 'POST':
        # Get the data from the form
        title = request.POST.get('title')
        content = request.POST.get('content')
        author_id = 3
        #generate slug  
        slug = title.replace(" ", "-")
    

        # Create a new Post object and save it to the database
        post = Post(title=title, content=content, author_id=author_id, slug=slug)
        post.save()

        # Redirect to the homepage
        return redirect('home')

    return render(request, 'new_post.html')

#create a method to generate a blog post from GPT-3 using the title of the new_post as the prompt
def new_post(request):
    if request.method == 'POST':
        # Get the data from the form
        title = request.POST.get('title')
        openai.api_key = "API KEY HERE"
        author_id = 1
        #Get current date and time
        now = datetime.datetime.now()
        #generate slug  
        slug = title.replace(" ", "-")
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt="A satirical news article about " +title +" in the style of the  Rueters. Ironic and wildly absurd at least 750 word long. Make sure its obviously satirical.",
            temperature=0.8,
            max_tokens=1000,
            top_p=1,
            frequency_penalty=.5,
            presence_penalty=.3,
            best_of = 5,
            )
        content = response['choices'][0]['text']
        post = Post(title=title, content=content, author_id=author_id, slug=slug, created_on=now)
        post.save()
        return redirect('fakenews')

    return render(request, 'new_post.html')

