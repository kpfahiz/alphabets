from django.db import models
from product.models import Product

class OrderItem(models.Model):
    order_item_quantity = models.IntegerField()
    item = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.item.name

class Order(models.Model):
    data_order_placed = models.DateField()
    order_item = models.ManyToManyField(OrderItem)

    def __str__(self):
        return str(self.data_order_placed)

class OrderStatus(models.Model):

    PACKED, SHIPPED, DELIVERED = 0,1,2
    ORDER_STATUS = [(PACKED, 'Packed'), (SHIPPED, 'Shipped'), (DELIVERED, 'Delivered')]
    order_status = models.SmallIntegerField(choices=ORDER_STATUS)
    order = models.ManyToManyField(Order)

    def __str__(self):
        return str(self.order_status)
