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
from django.contrib import messages
from django.views import View
from django.shortcuts import redirect
from django.db import transaction
from .models import Balance
from .forms import AmountForm
from .services import get_balance_by_user
from .services import create_new_balance_deposit, update_balance_by_deposit, deposit
from .services import withdraw

class LoginPage(LoginView):
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


class ServicesPage(LoginRequiredMixin, TemplateView):
    template_name = "atm/services.html"


class CheckBalancePage(LoginRequiredMixin, View):
    template = "atm/check-balance.html"

    def get(self, request):
        user_balance = get_balance_by_user(self.request.user)
        return render(request, self.template, {'user_balance': user_balance})


class DepositPage(LoginRequiredMixin, FormView):
    template_name = 'atm/deposit.html'
    form_class = AmountForm
    success_url = reverse_lazy('checkbalance')

    def form_valid(self, form):
        deposit(self.request.user, form.cleaned_data['amount'])
        return super().form_valid(form)


class WithdrawPage(LoginRequiredMixin, FormView):
    template_name = 'atm/withdraw.html'
    form_class = AmountForm
    success_url = reverse_lazy('withdraw')

    def form_valid(self, form):
        message = withdraw(self.request.user, form.cleaned_data['amount'])
        messages.success(self.request, message)
        return super().form_valid(form)
        
    


