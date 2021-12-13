'''
from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.contrib.auth import login, logout, get_user_model, authenticate
from django.contrib import messages
from django.http import HttpResponse
from .models import *
from django.conf import settings



User = settings.AUTH_USER_MODEL


# Create your views here.


def user_login(request):

    if request.method=='POST':
        user= get_user_model()
                
        username = request.POST['username']
        password = request.POST['password']
        
        authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
           return HttpResponse('Please provide the right informatiions and try again')
    else:
        return render(request, "login.html")
    
    



def signup(request):
    if request.method=='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        phone_number = request.POST['phone_number']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']
        
        
        
        if password==password1:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username taken')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email exists')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email exists')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username,  password=password, first_name=first_name, last_name=last_name, email=email, phone_number=phone_number,)
                user.save();
                login(request)
                return redirect('success')
                print('user created')
        else:
            messages.info(request, "Password doen't match")
            return redirect('signup')
        return redirect('/')
        
    else:    
        return render(request, "signup.html")
       
    

def logout(request):
    auth.logout(request)
    return redirect('/')
    
'''


from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.generic.detail import DetailView

from .forms import SignUpForm


class UserView(DetailView):
    template_name = 'profile.html'

    def get_object(self):
        return self.request.user


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(request, email=user.email, password=raw_password)
            if user is not None:
                login(request, user)
            else:
                print("user is not authenticated")
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})