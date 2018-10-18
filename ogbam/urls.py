from django.urls import path,include
from .import views


urlpatterns = [
    path('signup/',views.SignUp.as_view(),name='signup'),
    path('airtimecreate/',views.airtimeCreate.as_view(),name='airtime'),
    path('sharecreate/',views.shareCreate.as_view(),name='share'),
    path('withdrawCreate/',views.withdrawCreate.as_view(),name='withdraw'),
    path('history/',views.History.as_view(),name='history'),
    path('dataCreate/',views.dataCreate.as_view(),name='data'),
    
]