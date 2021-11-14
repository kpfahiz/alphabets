from django.db import models
from order.models import Order

class Customer(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    order_detials = models.ManyToManyField(Order, blank=True)
