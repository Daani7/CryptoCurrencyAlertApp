from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class CryptoAlert(models.Model):
    cryptocurrency = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    alert_type = models.CharField(max_length=10, default='', choices=[('above', 'Au-dessus de'), ('below', 'En dessous de')])
    name = models.CharField(max_length=100, default='')
    created_date = models.DateTimeField(auto_now_add=True)
    message = models.CharField(max_length=255, blank=True, null=True)
    email_sent = models.BooleanField(default=False)
    user = models.ForeignKey(User,default='', on_delete=models.CASCADE, related_name='alerts')

    def __str__(self):
        return f"{self.cryptocurrency}"
