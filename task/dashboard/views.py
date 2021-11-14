from django.shortcuts import render

from customer.models import Customer



def quotesview(request):
    '''
    View for quotes informations
    '''
    
    queryset    = Customer.objects.all()
    context     = {
        'queryset': queryset,
    }
    return render(request, 'dashboard.html',context=context)
    
def clientview(request):
    '''
    View for client details
    '''
    queryset    = Customer.objects.all()
    context     = {
        'queryset': queryset,
    }
    return render(request, 'client.html',context=context)