from django.db import models
from order.models import OrderStatus

class Customer(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    order_detials = models.ManyToManyField(OrderStatus, blank=True)

    def __str__(self):
        return self.user.username
