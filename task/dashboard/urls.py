from django.urls import path, include

from .views import quotesview, clientview


urlpatterns = [
    path('', quotesview, name='quotes'),
    path('client/', clientview, name='client'),

]