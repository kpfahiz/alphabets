from django.db import models

from product.models import Product


class SupplierProduct(models.Model):
    product = models.ManyToManyField(Product)

    def __str__(self):
        return str(self.product.name)
class Supplier(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    supplier_product = models.ManyToManyField(SupplierProduct, blank=True)


    def __str__(self):
        return str(self.user.username)