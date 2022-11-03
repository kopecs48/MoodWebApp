from django.shortcuts import render, redirect

# Create your views here.


def home(request):
    #nothing to see on hompage so send them to mood endpoint
    return redirect('accounts:mood')