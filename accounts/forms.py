from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    content = forms.CharField(required=True)
    #the only fields they have access to type into are content and title
    #the rest are autofilled on the backend
    class Meta:
        model = Post
        exclude = ("author", "slug", "streak" )