from django.shortcuts import render

from customer.models import Customer



def quotesview(request):
    
    queryset = Customer.objects.all()
    context = {
        'queryset': queryset,
    }
    return render(request, 'dashboard.html',context=context)
    
def clientview(request):
    queryset = Customer.objects.all()
    context = {
        'queryset': queryset,
    }
    return render(request, 'client.html',context=context)