from django.db import models
from product.models import Product

class OrderItem(models.Model):
    '''
    The order item is a product with a quantity.
    '''
    order_item_quantity         = models.IntegerField()
    item                        = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.item.name

class Order(models.Model):
    '''
    The order is a list of order items and order placed date.
    '''
    data_order_placed           = models.DateField()
    order_item                  = models.ManyToManyField(OrderItem)

    def __str__(self):
        return str(self.data_order_placed)

class OrderStatus(models.Model):
    '''
    The order status is a list of orders.
    '''
    PACKED, SHIPPED, DELIVERED  = 0,1,2
    ORDER_STATUS                = [(PACKED, 'Packed'), (SHIPPED, 'Shipped'), (DELIVERED, 'Delivered')]
    
    order_status                = models.SmallIntegerField(choices=ORDER_STATUS)
    order                       = models.ManyToManyField(Order)

    def __str__(self):
        return str(self.order_status)
