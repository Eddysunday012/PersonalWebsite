import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.

def home(request):
    return render(request, 'base/home.html')

def projects(request):
    return render(request, 'base/projects.html')

