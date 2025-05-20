from django.db import models
from goods.models import Goods

class Warehouse(models.Model):
    goods = models.OneToOneField(
        Goods,
        primary_key=True,
        on_delete=models.CASCADE
    )
    amount = models.BigIntegerField()

