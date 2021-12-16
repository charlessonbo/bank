from django.urls import path
from .views import LoginPage, RegisterPage, ServicesPage, DepositPage, CheckBalancePage, WithdrawPage
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', ServicesPage.as_view(), name='services'),
    path('login/', LoginPage.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('checkbalance/', CheckBalancePage.as_view(), name='checkbalance'),
    path('deposit/', DepositPage.as_view(), name='deposit'),
    path('withdraw/', WithdrawPage.as_view(), name='withdraw'),
]