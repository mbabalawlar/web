from django.shortcuts import render
from django.views import generic
# Create your views here.
from django.urls import reverse_lazy
from .forms import *
from .models import CustomUser
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView 
from django.contrib.auth import get_user_model
from django.db.models import F

# Create your views here.

class UserView(TemplateView ):
    template_name='home.html'
    
    
    def get_context_data(self,**kwargs):
        context = super(UserView,self).get_context_data(**kwargs)
        context['airtime'] = Airtime.objects.filter(user=self.request.user)
        context['withdraw'] = withdraw.objects.filter(user=self.request.user)
        
        return context

class History(TemplateView):
    template_name='history.html'
    
    
    def get_context_data(self,**kwargs):
        context = super(History,self).get_context_data(**kwargs)
        context['airtime'] = Airtime.objects.filter(user=self.request.user)
        context['withdraw'] = withdraw.objects.filter(user=self.request.user)
        context['Data'] = Data.objects.filter(user=self.request.user)
        context['share and sell'] = Share_And_Sell.objects.filter(user=self.request.user)
        
        return context


class HomeView(generic.DetailView):
    model = CustomUser
    template_name = 'detail.html'
    
    
class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

    
class airtimeCreate(generic.CreateView):
    form_class = airtimeform
    success_url = reverse_lazy('login')
    template_name = 'airtime_form.html'

    def form_valid(self,form):
        object = form.save(commit=False)
        object.user = self.request.user
        form.save()
        return super(airtimeCreate,self).form_valid(form)

    
class shareCreate(generic.CreateView):
    form_class = shareform
    success_url = reverse_lazy('login')
    template_name = 'share_and_sell_form.html'

    def form_valid(self,form):
        object = form.save(commit=False)
        object.user = self.request.user
        form.save()
        return super(shareCreate,self).form_valid(form)

class withdrawCreate(generic.CreateView):
    form_class = withdrawform
    success_url = reverse_lazy('login')
    template_name = 'withdraw_form.html'

    def form_valid(self,form):
        object = form.save(commit=False)
        object.user = self.request.user
        form.save()
        return super(withdrawCreate,self).form_valid(form)

class dataCreate(generic.CreateView):
    form_class = dataform
    success_url = reverse_lazy('login')
    template_name = 'data_form.html'

    def form_valid(self,form):
        object = form.save(commit=False)
        object.user = self.request.user
        form.save()
        return super(dataCreate,self).form_valid(form)
