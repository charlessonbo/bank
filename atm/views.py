from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.views import View
from django.shortcuts import redirect
from django.db import transaction
from .models import Balance
from .forms import AmountForm


class CustomLoginView(LoginView):
    template_name = 'atm/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('services')


class RegisterPage(FormView):
    template_name = 'atm/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('services')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)


class TaskList(LoginRequiredMixin, TemplateView):
    template_name = "atm/services.html"


class Deposit(LoginRequiredMixin, FormView):
    template_name = 'atm/deposit.html'
    form_class = AmountForm
    success_url = reverse_lazy('services')

    def form_valid(self, form):
        user_balance = None

        try:
            user_balance = Balance.objects.get(user=self.request.user)
        except Balance.DoesNotExist:
            pass
     
        if not user_balance:
            user_balance = Balance(user=self.request.user, balance=float(form.cleaned_data['amount']))
            user_balance.save()
            return super().form_valid(form)
        
        user_balance.balance = float(user_balance.balance) + float(form.cleaned_data['amount'])
        user_balance.save()
        return super().form_valid(form)
        
    


