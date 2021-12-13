from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User






# Create your models here.


class Balance(models.Model):
    id = models.AutoField(primary_key = True, default = 0)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bonus = models.FloatField(default = 0.000)
    capital =  models.FloatField(default = 0.000)
    asset =  models.IntegerField(default = 0)
    profit = models.FloatField(default = 0.000)
    btc =  models.FloatField(default = 0.00000000)
    usd =  models.FloatField(default = 0.000)
    
    def __str__(self):
        return str(self.user)
 
 
trans_type = (
    ('Withdraw', 'WD'),
    ('Deposit', 'Dp'),
)
        
class Transaction(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=False)
    created = models.DateField(default = timezone.now)
    amount =  models.FloatField(default = 0.000,  primary_key = True,)
    tp =  models.CharField(max_length=15, choices=trans_type,  blank=False)
    
    def __str__(self):
        return str(self.user)
        

