from django.db import models


class Goods(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)
    goods_parameter = models.JSONField()
    credit = models.DecimalField(max_digits=6, decimal_places=2)
