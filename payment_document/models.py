from django.db import models
from enum import Enum, IntEnum

from app_support_place.generic_class.mixins import CreatedUpdatedMixin
from payment_gateway.models import PaymentGateway


class PaymentDocumentConfirm(IntEnum):
    invoice = 1
    recipt_of_payment = 2

class Paycheck(IntEnum):
    cash = 1
    bank_transfer = 2

class CreditContract(
    models.Model,
    CreatedUpdatedMixin
):
    html_contract = models.TextField() # save as html
    plain_text_contract = models.TextField()
    file = models.BinaryField()
    extension = models.CharField(max_length=10)

class PaymentDocument(
    models.Model,
    CreatedUpdatedMixin
):
    gateway = models.ForeignKey(
        PaymentGateway,
        on_delete=models.DO_NOTHING
    )
    confirm = models.IntegerChoices(PaymentDocumentConfirm)
    paycheck = models.IntegerChoices(Paycheck)
    on_credit = models.BooleanField(default=False)
    credit_contract = models.OneToOneField(
        CreditContract,
        on_delete=models.CASCADE
    )