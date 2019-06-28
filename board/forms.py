from django import forms
from .models import Post, Comment, SubComment
from account.models import User

class CreatePostForm(forms.ModelForm):
    class Meta:
    model = Post
    fields= __all__
