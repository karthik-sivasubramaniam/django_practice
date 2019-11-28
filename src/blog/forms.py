from django import forms
from .models import BlogPost

class CreatePostModelForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'slug', 'content']