from django.urls import path
from .views import Services, Deposit, CustomLoginView, RegisterPage, CheckBalance
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('', Services.as_view(), name='services'),
    path('checkbalance/', CheckBalance.as_view(), name='checkbalance'),
    path('deposit/', Deposit.as_view(), name='deposit'),
]