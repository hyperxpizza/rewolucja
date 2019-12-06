from django.db import models
from decimal import Decimal
from payments import PurchasedItem
from payments.models import BasePayment

class Payment(BasePayment):
    pass