from django.db import models
from order.models import OrderStatus

class Address(models.Model):
    '''
    The address is a street, city, state, zip, and country.
    '''
    address         = models.CharField(max_length=255)
    city            = models.CharField(max_length=255)
    state           = models.CharField(max_length=255)
    zip_code        = models.CharField(max_length=255)
    country         = models.CharField(max_length=255)
    phone_number    = models.CharField(max_length=255)

class Customer(models.Model):
    '''
    The customer is a user with an address.
    '''
    user            = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    order_detials   = models.ManyToManyField(OrderStatus, blank=True)
    address         = models.ForeignKey(Address, on_delete=models.CASCADE, null=True)
    profile_url     = models.CharField(max_length=2083)

    def __str__(self):
        return self.user.username
