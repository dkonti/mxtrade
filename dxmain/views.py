from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from Balance.models import *
from django.contrib.auth.models import User
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError, EmailMessage
from django.http import HttpResponse
from django.conf import settings


# Create your views here.


def home(request):
	#return HttpResponse("about")
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        main = str(message)
        
        send_mail('Contact Form from ' + str(name), main, email, ['dxtradeinvestment@gmail'], fail_silently=False)
    return render(request, "index.html")
    

    
def services(request):
	#return HttpResponse("about")
    return render(request, "services.html")    
    
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        main = str(message)
        
        send_mail('Contact Form from ' + str(name), main, email, ['dxtradeinvestment@gmail'], fail_silently=False)
        
    return render(request, "contact.html")

    
def subscribe(request):
    if request.method == 'POST':
        package = request.POST.get('package')
        current_user =request.user
        message = 'I want to Subscribe to' + package + ' from ' + str(current_user)
        
        send_mail('Subscribe', message, settings.EMAIL_HOST_USER, ['mxtradeinvest@outlook.com'], fail_silently=False)
        
        return redirect('success1')
    return render(request, "subscribe.html")
    
def success(request):
	#return HttpResponse("about")
    return render(request, "success.html")
    
def success1(request):
	#return HttpResponse("about")
    return render(request, "success1.html")


       
