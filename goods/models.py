from django.db import models

from app_support_place.generic_class.mixins import CreatedUpdatedMixin

class GoodsBrand(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    logo = models.ImageField(upload_to='brands/', null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class GoodsCategory(
    models.Model,
    CreatedUpdatedMixin
):
    name = models.CharField(max_length=150)
    number = models.BigIntegerField()

    class Meta:
        unique_together = ('name', 'number')


class Goods(
    models.Model,
    CreatedUpdatedMixin
):
    name = models.CharField(
        max_length=150,
        null=False,
        blank=False
    )
    slug = models.SlugField(unique=True)
    goods_parameter = models.JSONField()
    credit = models.DecimalField(
        max_digits=6,
        decimal_places=2
    )
    category = models.ForeignKey(
        GoodsCategory,
        on_delete=models.DO_NOTHING
    )

    class Meta:
        unique_together = ('name', 'goods_parameter')

class GoodsParametersTemplate(
    models.Model,
    CreatedUpdatedMixin
):
    category = models.OneToOneField(
        GoodsCategory,
        on_delete=models.CASCADE
    )
    goods_parameter_template = models.JSONField()

    class Meta:
        unique_together = ('category', 'goods_parameter_template',)