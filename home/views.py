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
    template_name = 'home/projects.html'

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
        prompt = "A satirical blog post about " +title + "in the style of the onion. Make i funny and interesting. The post should be about 500 words long. Make sure its obviously satirical."
        openai.api_key = "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"
        author_id = 1
        #Get current date and time
        now = datetime.datetime.now()
        #generate slug  
        slug = title.replace(" ", "-")
        image = openai.Image.create(
                prompt = title,
                n = 1,
                size="512x512"
                )
        image_url = image['data'][0]['url']
        while(image_url == None):
            os.sleep(1)
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt="A satirical news article about " +title +" in the style of the Onion pretending to be Rueters. Ironic and absurd at least 1000 word long. Make sure its obviously satirical. Give it a headline and a subhead. Make sure it wraps up with a punchline.",
            temperature=0.8,
            max_tokens=1000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            best_of = 8,
            )
        content = response['choices'][0]['text']
        post = Post(title=title, content=content, author_id=author_id, slug=slug, created_on=now, image_url=image_url)
        post.save()
        return redirect('projects')

    return render(request, 'new_post.html')

