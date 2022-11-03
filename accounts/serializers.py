from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    #the only fields we want to serialize are the ones listed in the meta, because they are needed to
    # make the mood post list
    author = serializers.ReadOnlyField(source='author.username')
    class Meta:
        model = Post
        fields = ['title', 'author', 'content', 'created_on', 'created_time', 'streak']