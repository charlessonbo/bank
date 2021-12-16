
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Balance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    balance = models.DecimalField(max_digits = 30, decimal_places = 2)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.balance)
