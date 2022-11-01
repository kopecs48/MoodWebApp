from email.policy import default
from django.db import models
from django.contrib.auth.models import User



class Post(models.Model):
    title = models.CharField(max_length=200, unique=False)
    # slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    content = models.TextField()
    created_on = models.DateField(auto_now_add=True)
    streak = models.IntegerField(default=1)
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
