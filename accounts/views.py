from urllib import request
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from rest_framework import generics
from . import serializers
from .models import Post
from django.http import JsonResponse
import django_filters.rest_framework
from datetime import date
from datetime import timedelta


# Create your views here.


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            #log user in
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            #log user in
            return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
    return redirect('accounts:login')

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("/")
    form = PostForm()
    return render(request, "post.html", {"form": form})


# class PostList(generics.ListCreateAPIView):
    
#     serializer_class = serializers.PostSerializer
#     # permission_classes = (IsAuthenticated,)
    
#     def get_queryset(self):
#         """
#         This view should return a list of all the purchases
#         for the currently authenticated user.
#         """
        
#         user = self.request.user
#         return Post.objects.filter(author=user)

    
#     def perform_create(self, serializer):
#         # serializer.author = self.request.user.id
#         # serializer.save()
        
#         form = PostForm(data=self.request.data)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = self.request.user
#             post.save()
#             return redirect("accounts:mood")

@login_required
def post_list(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            prevPosts = Post.objects.filter(author=request.user)
            if prevPosts:
                prev = prevPosts[0]
                today = date.today()
                yesterday = today - timedelta(days=1)
                prev_date = prev.created_on
                if prev.created_on == today:
                    post.streak = prev.streak
                elif prev.created_on == yesterday:
                    post.streak = prev.streak + 1
                else:
                    post.streak = 1
            else:
                post.streak = 1
            post.save()
            return redirect("accounts:mood")
    form = PostForm()
    posts = Post.objects.filter(author=request.user)
    serializer = serializers.PostSerializer(posts, many=True)
    return render(request, "mood.html", {"form": form, "posts": serializer.data})

