from datetime import datetime
from pydantic import BaseModel
from enum import Enum, IntEnum

# for development


class PaymentMethods(BaseModel):
    site_amount: int
    database_support: bool
