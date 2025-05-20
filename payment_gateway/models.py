from django.db import models

from app_support_place.generic_class.mixins import CreatedUpdatedMixin


class PaymentGateway(
    models.Model,
    CreatedUpdatedMixin
):
    gateway = models.CharField(max_length=100, unique=True)
    secure = models.BooleanField(default=True)
    configuration = models.JSONField()