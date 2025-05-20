from django.db import models
from goods.models import Goods
from warehouse.models import Warehouse


class Exhibit(models.Model):
    goods = models.ForeignKey(
        Goods,
        on_delete=models.DO_NOTHING
    )
    credit = models.DecimalField(
        max_digits=6,
        decimal_places=2
    )
    warehouse = models.OneToOneField(
        Warehouse,
        on_delete=models.DO_NOTHING
    )

    def save(
        self,
        *args,
        **kwargs,
    ):
        self.warehouse = self.goods
        super().save(*args, **kwargs)