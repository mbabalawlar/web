from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import *
from .models import *

class CustomUserAdmin(UserAdmin):
    add_form=CustomUserCreationForm
    form = CustomUserChangeForm
    list_display =['username','email','birth_date','BankName','AccountNumber','Phone','Account_Balance']
    '''
    fieldsets = (
    
        ('info', {
            'fields': ('username','email','birth_date','BankName','AccountNumber','Phone'  ),
        }),   
    )'''
   
class AirtimeAdmin(admin.ModelAdmin):
    add_form=airtimeform
    list_display =['user','network','mobile_number','pin','amount','Status']
 
class DataAdmin(admin.ModelAdmin):
    add_form=dataform
    list_display =['network','mobile_number','plan','method','Status']

class ShareAdmin(admin.ModelAdmin):
    add_form=shareform
    list_display =['network','mobile_number','amount','Status']

class WithdrawAdmin(admin.ModelAdmin):
    add_form=withdrawform
    list_display =['accountNumber','accountName','bankName','amount','Status']

 

admin.site.register(CustomUser,CustomUserAdmin)
admin.site.register(Airtime,AirtimeAdmin)
admin.site.register(Data,DataAdmin)
admin.site.register(Share_And_Sell,ShareAdmin)
admin.site.register(Withdraw,WithdrawAdmin)
