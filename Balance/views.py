from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail, BadHeaderError, EmailMessage
from django.views import generic
from django.conf import settings
from .models import *

# Create your views here.


@login_required   
def wallet(request):
	#return HttpResponse("about")
    #valuenext=request.POST.get('next')
    #user = Balance.objects.all()
    balance = Balance.objects.all()
    return render(request, 'dashboard.html', {'balance':balance})
    
@login_required     
def transaction(request):
    transaction = Transaction.objects.all()
	#return HttpResponse("about")
    return render(request, "transaction.html", {'transaction':transaction})
    
@login_required 
def payment(request):
    if request.method == 'POST':
        amount = request.POST.get('asset')
        current_user =request.user
        message = 'I want to make a payment of ' + str(amount) + ' btc from ' + str(current_user)
        
        send_mail('BTC deposit', message, settings.EMAIL_HOST_USER, ['mxtradeinvest@outlook'], fail_silently=False)
        
        return redirect('success')
        
    return render(request, "payment.html")
    

@login_required 
def deposit(request):
    if request.method == 'POST':
        amount = request.POST.get('asset')
        current_user =request.user
        message = 'I want to make a deposit of $' + str(amount) + ' from ' + str(current_user)
        
        send_mail('Deposit', message, settings.EMAIL_HOST_USER, ['mxtradeinvest@outlook'], fail_silently=False)
        
        return redirect('payment')
        
    return render(request, "deposit.html")

@login_required 
def withdraw(request):
    if request.method == 'POST':
        amount = request.POST.get('asset')
        address = request.POST.get('addresss')
        current_user =request.user
        message = 'I want to make a withdrawal of ' + str(amount) + ' BTC from ' + str(current_user) + 'to my wallet: ' + str(address)
        
        send_mail('Deposit', message, settings.EMAIL_HOST_USER, ['mxtradeinvest@outlook'], fail_silently=False)
        
        return redirect('success')
        
    return render(request, "withdraw.html")
    
    
    
'''class WalletView(generic.WalletView):
    model = Balance
    template_name = 'polls/detail.html'
    def get_queryset(self): 
        """ Excludes any questions that aren't published yet. """ 
        return Balance.objects.all()'''