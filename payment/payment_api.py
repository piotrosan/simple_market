from abc import ABC


class PaymentServiceAbstract(ABC):
    pass


class PaymentService:
    pass


class PaymentCreditCard(
    PaymentService,
    PaymentServiceAbstract
):
    pass


class PaymentBankTransfer(
    PaymentService,
    PaymentServiceAbstract
):
    pass


