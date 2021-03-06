from django.db import models


class Product(models.Model):
    '''
    The product is a product with a name, price, and description.
    '''
    number          = models.IntegerField()
    name            = models.CharField(max_length=255)
    price           = models.FloatField()
    stock           = models.IntegerField()
    image_url       = models.CharField(max_length=2083)

    def __str__(self):
        return self.name
