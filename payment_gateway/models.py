from django.db import models

# Create your models here.

class PaymentGateway(models.Model):
    gateway = models.CharField(max_length=100)
    secure = models.BooleanField(default=True)
    configuration = models.JSONField()