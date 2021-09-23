from django.shortcuts import render, redirect

# Create your views here.

def sendEmail(request):
    return render(request, 'sendemail/email.html')
