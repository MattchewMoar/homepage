from django import forms

class BlogPostForm(forms.Form):
    user_input = forms.CharField(widget=forms.Textarea)