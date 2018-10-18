from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import *


status =(
    ('pending','Pending'),
    ('failed','Failed'),
    ('successful','Successful'),
)

Airtime_choice =(
    (100 , '#100'),
    (500,'#500'),
    (1000,'#1000'),
    (5000,'#5000'),
    (1000,'#1000'),
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

Bank =(
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

Network =(
    ('mtn','MTN'),
    ('glo','GLO'),
    ('airtel','AIRTEL'),
    ('etisalate','ETISALAT'),
   
)

Paying_method  = (
    ('Airtime Pin','Airtime Pin'),
    ('Bank  Transfer','Bank Transfer'),
    ('Wallet','Wallet'),
    ('Airtime tranfer','Airtime tranfer'),
  
)

class CustomUserCreationForm(UserCreationForm):
    username  = forms.CharField() 
    password1 = forms.CharField(widget = forms.PasswordInput, label='Password',
    help_text='min_lenght-8 mix characters [i.e musa1234] ')
    password2 = forms.CharField(widget = forms.PasswordInput,help_text='Enter same password as before',
     label='Comfirm Password')
    BankName =  forms.ChoiceField(choices=Bank)
    AccountNumber = forms.IntegerField(max_value=9999999999)
    Phone = forms.IntegerField(label='Phone +234',max_value=99999999999)
    birth_date = forms.DateField(help_text='required.FORMAT:YYYY-MM-DD[1998-10-19]')

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username','email','birth_date','BankName','AccountNumber','Phone','password1','password2')

class CustomUserChangeForm(UserChangeForm):
    
    class Meta(UserChangeForm.Meta):
        model = CustomUser
        fields = ('username','email','birth_date','BankName','AccountNumber','Phone')

class airtimeform(forms.ModelForm):
    
    
    mobile_number = forms.IntegerField(label='Phone +234', max_value=999999999999)
    pin = forms.IntegerField(label='Recharge Pin:')
    amount = forms.ChoiceField(choices=Airtime_choice,initial='#100')
    
    
    class Meta:
        model = Airtime
        fields = ('network','mobile_number','pin','amount')


class shareform(forms.ModelForm):
     network = forms.ChoiceField(choices=Network,initial='MTN')
    
     class Meta:
        model = Share_And_Sell
        fields = ('network','mobile_number','amount')


class withdrawform(forms.ModelForm):
     bankName = forms.ChoiceField(choices=Bank,initial='UBA')
     class Meta:
        model = Withdraw
        fields =  ('accountNumber','accountName','bankName','amount')

class dataform(forms.ModelForm):
     network = forms.ChoiceField(choices=Network,initial='MTN')
     plan = forms.ChoiceField(choices=Data_plan,initial='MTN  1GB  #800',required=True)
     method =  forms.ChoiceField(choices=Paying_method)
     mobile_number = forms.IntegerField(label='Phone +234', max_value=999999999999)
    
     class Meta:
        model = Data
        fields =  ('network','mobile_number','plan','method')
