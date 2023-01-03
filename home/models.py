from django.db import models
from django.contrib.auth.models import User


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

class Bio(models.Model):
    name = models.CharField(max_length=200, unique=True)
    education = models.TextField()
    experience = models.TextField()
    about = models.TextField()
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='bio')

    def __str__(self):
        return self.name

class ContactInfo(models.Model):
    name = models.CharField(max_length=200, unique=True)
    email = models.EmailField(max_length=200, unique=True)
    linkin = models.URLField(max_length=200, unique=True)
    github = models.URLField(max_length=200, unique=True)
    discord = models.URLField(max_length=200, unique=True)
    facebook = models.URLField(max_length=200, unique=True, default="https://www.facebook.com/profile.php?id=100050463701271")
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='contact_posts')

    def __str__(self):
        return self.name