from django.contrib import admin
from .models import Post, Bio, ContactInfo

admin.site.register(Post)
admin.site.register(Bio)
admin.site.register(ContactInfo)