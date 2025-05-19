from django.db import models
from goods.models import Goods

class Warehouse(models.Model):
    goods = models.OneToOneField(Goods, on_delete=models.CASCADE)
    amount = models.BigIntegerField()

