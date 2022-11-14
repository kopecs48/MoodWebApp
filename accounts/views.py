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

#create new account if all required data is there and meets signup criteria
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        #create form with posted data and check if it is valid
        if form.is_valid():
            user = form.save()
            login(request, user)
            #log user in and redirect to mood endpoint
            return redirect('accounts:mood')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

#log in user if they are posting to this endpoint and all data is authenticated
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        #if all data is proper and correct login to current seesion and redirect to mood endpoint
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            #log user in
            return redirect('accounts:mood')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

#log out the current user and redirect back to login
def logout_view(request):
    if request.method == 'POST':
        logout(request)
    return redirect('accounts:login')

#test method
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


@login_required
def post_list(request):
    #track today and yesterday for current streak field later
    today = date.today()
    yesterday = today - timedelta(days=1)
    #if someone is posting a mood
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        #validate form
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            prevPosts = Post.objects.filter(author=request.user)
            #if there are previous posts from the user we want to know if any are from the day before
            if prevPosts:
                prev = prevPosts[0]
                prev_date = prev.created_on
                #keep current streak if post is from today, increment if from yesterday
                #else default back to 1
                if prev.created_on == today:
                    post.streak = prev.streak
                elif prev.created_on == yesterday:
                    post.streak = prev.streak + 1
                else:
                    post.streak = 1
            else:
                post.streak = 1
            post.save()
            #save post and do a get call on the mood endpoint
            return redirect("accounts:mood")
    #create new form 
    form = PostForm()
    posts = Post.objects.filter(author=request.user)
    #set current to 0 which will only stay 0 if there is no post from the day before
    streak = 0
    if posts:
        last = posts[0]
        if last.created_on == yesterday or last.created_on == today:
            streak = last.streak
    #serialize all data from the post db
    serializer = serializers.PostSerializer(posts, many=True)   
    return render(request, "mood.html", {"form": form, "posts": serializer.data, "streak": streak})

