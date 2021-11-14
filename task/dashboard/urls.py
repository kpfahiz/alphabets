from django.urls import path, include

from .views import quotesview


urlpatterns = [
    path('', quotesview, name='quotes'),

]