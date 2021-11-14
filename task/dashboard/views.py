from django.shortcuts import render

from order.models import Order, OrderStatus



def quotesview(request):
    
    queryset = Order.objects.all()
    x=[1,2,3,4]
    context = {
        'queryset': queryset,
        'x': x
    }
    for i in queryset:
        print(i.data_order_placed)
        for j in i.order_item.all():
            print(j.order_item_quantity)
    return render(request, 'dashboard.html',context=context)
    
