from django.shortcuts import render, redirect
from django.core.mail import send_mail

# Create your views here.

def sendEmail(request):
    
    if(request == "POST"):
        send_mail()
    
    else:
        return render(request, 'sendemail/email.html')
