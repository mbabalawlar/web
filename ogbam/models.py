from django.db import models
from django.db.models import F
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils import timezone
import requests
# Create your models here.

User = settings.AUTH_USER_MODEL

Bank = (
    ('first bank','First Bank of Nigeria'),
    ('uba','UBA'),
    ('access','Access Bank'),
    ('wema','Wema Bank'),
    ('diamond','Diamond Bank'),
    ('heritage','Heritage bank'),
    ('sky','Sky Bank'),
    ('stanbic','Stanbic IBTC'),
    ('sterling','Sterling Bank'),
    ('union','Union Bank'),
    ('zenith','Zenith Bank'),
    ('unity','Unity Bank'),
    ('fcmb','FCMBank'),
    ('gtb','GTBank'),
    ('fidelity','FIdelity Bank'),
    ('eco','ECO Bank'),

)
status =(
    ('pending','Pending'),
    ('failed','Failed'),
    ('successful','Successful'),
)

Network =(
    ('mtn','MTN'),
    ('glo','GLO'),
    ('airtel','AIRTEL'),
    ('etisalate','ETISALAT'),
    
)
Data_plan  = (
    ('mtn_1gb','MTN  1GB  #800'),
    ('mtn_2gb','MTN  2GB  #1,550'),
    ('mtn_3gb','MTN  3GB  #2,250'),
    ('mtn_5gb','MTN  5GB  #3,750'),

    ('9mobile_1gb','9MOBILE  1GB  #700'),
    ('9mobile_1.5gb','9MOBILE  1.5GB  #1,050'),
    ('9mobile_2gb','9MOBILE  2GB  #1,400'),
    ('9mobile_3gb','9MOBILE  3GB  #2,000'), 
    ('9mobile_5gb','9MOBILE  5GB  #3,500'),
    ('9mobile_11gb','9MOBILE 11GB  #7,500'), 

    ('airtel_1.5gb','AIRTEL 1.5GB #900'),
    ('airtel_3.5gb','AIRTEL 3.5GB #1,0850'),
    ('airtel_5gb','AIRTEL 5GB #2,330'),
    ('airtel_7gb','AIRTEL 7GB #3,300'),


    ('glo_1.6gb','GLO 1.6/2GB 900#'),
    ('glo_3.65gb','GLO 3333.65/4.5GB  2,250#'),
    ('glo_5.7gb','GLO 5.7/7.2GB #2,650'),
    ('glo_10gb','GLO 10/12.5GB #3,550'),
    ('glo_20gb','GLO 20GB #7,000'),
    ('glo_26gb','GLO 26GB #8000'),
    ('glo_42gb','GLO 42GB #13,000'),
    
    
)
Paying_method  = (
    ('Airtime Pin','Airtime Pin'),
    ('Bank  Transfer','Bank Transfer'),
    ('Wallet','Wallet'),
    ('Airtime tranfer','Airtime tranfer'),
    
)
Airtime_choice =(
    ('100' , '#100'),
    ('500','#500'),
    ('1000','#1000'),
    ('5000','#5000'),
    ('1000','#1000'),
)

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length = 50 ,blank=True,null=True)
    birth_date = models.DateField(blank=True,null=True)
    BankName = models.CharField(max_length = 100, choices=Bank, blank=True)
    AccountNumber = models.CharField(max_length = 30 ,blank=True)
    Phone = models.CharField(max_length = 30 ,blank=True)
    AccountName = models.CharField(max_length = 30 ,blank=True)
    Account_Balance = models.FloatField(default=0.00,null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


    def __str__(self):
        return self.username + '----' + str(self.Phone)


    def deposite(self,amount):
        self.Account_Balance += amount
        self.save()

    def withdraw(self,amount):
           self.Account_Balance -= amount
           self.save()

    


class Plan(models.Model):
    user= models.ForeignKey(User, on_delete = models.CASCADE,null=True)
    network = models.CharField(max_length=30,choices=Network,default='MTN')
    plan_data =  models.CharField(max_length = 30, blank=True)
    plan_amount = models.CharField(max_length = 30, blank=True)
    month_validate  = models.CharField(max_length = 30, blank=True)

    def __str__(self):
        return self.plan_data


class Share_And_Sell(models.Model):
      user= models.ForeignKey(User, on_delete = models.CASCADE,editable=False,blank=False,null=True)
      network = models.CharField(max_length=30,choices=Network,default='MTN')
      mobile_number = models.CharField(max_length = 30, blank=True)
      amount =models.FloatField()
      Status =models.CharField(max_length=30,choices=status,default='Pending')
      create_date  = models .DateTimeField(default=timezone.now())

      def create(self):
         self.create_date = timezone.now()
         self.save()

      
      def __str__(self):
       return self.mobile_number

      def save(self,*args,**kwargs):
             if self.Status == 'successful':
                mb = CustomUser.objects.get( email = self.user.email)
                mb.deposite(float(self.amount))
             super(Share_And_Sell,self).save(*args,**kwargs)
       
     
      
class Airtime(models.Model):
    
     user= models.ForeignKey(User, on_delete = models.CASCADE,editable=False,blank=False,null=True)
     network = models.CharField(max_length=30,choices=Network,default='MTN')
     pin = models.CharField(max_length = 30, blank=True)
     mobile_number = models.CharField(max_length = 30, blank=True)
     amount = models.CharField(max_length = 30,choices=Airtime_choice, default='#100')
     Status =models.CharField(max_length = 30,choices=status, default='Pending')
     create_date  = models .DateTimeField(default=timezone.now())

     def create(self):
         self.create_date = timezone.now()
         self.save()

    
     def __str__(self):
         return self.mobile_number

     def save(self,*args,**kwargs):
              if self.Status == 'successful':
                    mb = CustomUser.objects.get( email = self.user.email)
                    mb.deposite(float(self.amount))
              super(Airtime,self).save(*args,**kwargs)
       
        

class Withdraw(models.Model):
    user= models.ForeignKey(User, on_delete = models.CASCADE,editable=False,blank=False,null=True)
    accountNumber = models.CharField(max_length = 30, blank=True)
    accountName = models.CharField(max_length = 30, blank=True)
    bankName = models.CharField(max_length = 100, choices=Bank, blank=True)
    amount = models.CharField(max_length = 30, blank=True)
    Status =models.CharField(max_length=30,choices=status,default='Pending')
    create_date  = models .DateTimeField(default=timezone.now())

    def create(self):
         self.create_date = timezone.now()
         self.save()

    def clean(self):
        mb = CustomUser.objects.get( email = self.user.email)
        if self.amount > mb.Account_Balance:
               raise ValidationError

    def save(self,*args,**kwargs):
              if self.Status == 'successful':
                    mb = CustomUser.objects.get( email = self.user.email)
                    mb.withdraw(float(self.amount))
              super(Withdraw,self).save(*args,**kwargs)
          
    def __str__(self):
             return self.accountName
 

class Data(models.Model):
     user= models.ForeignKey(User, on_delete = models.CASCADE,editable=False,blank=False,null=True)
     network = models.CharField(max_length=30,choices=Network,default='MTN')
     plan = models.CharField(choices=Data_plan,max_length=50, null=True)
     mobile_number = models.CharField(max_length = 30, blank=True)
     method =  models.CharField(max_length = 30, choices=Paying_method, blank=True)
     Status =models.CharField(max_length = 30, choices = status,default='Pending')
     create_date  = models .DateTimeField(default=timezone.now())

     def create(self):
         self.create_date = django.utils.timezone.now()
         self.save()

     def __str__(self):
              return self.plan