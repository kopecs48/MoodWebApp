from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    content = forms.CharField(required=True)

    class Meta:
        model = Post
        exclude = ("author", "slug", "streak" )