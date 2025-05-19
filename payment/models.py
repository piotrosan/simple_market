from django.db import models

# Create your models here.


class PaymentGateway(models.Model):
    gateway = models.CharField()
    secure = models.BooleanField()
    methods = models.JSONField()
