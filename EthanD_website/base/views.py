from django.shortcuts import render, redirect

# Create your views here.

def home(request):
    return render(request, 'base/home.html')

def projects(request):
    return render(request, 'base/projects.html')