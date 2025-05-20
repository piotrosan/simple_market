from django.db import models
from goods.models import Goods
from user_profile.models import MarketUser


class Warehouse(models.Model):
    goods = models.OneToOneField(
        Goods,
        primary_key=True,
        on_delete=models.CASCADE
    )
    amount = models.BigIntegerField()
    provider = models.ForeignKey(
        MarketUser,
        on_delete=models.DO_NOTHING
    )

