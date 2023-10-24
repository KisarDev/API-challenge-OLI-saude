from django.urls import path
from api.views import create_customer, list_customer_id, list_customer, edit_customer, customer_with_greatrisk

urlpatterns = [
    path('create_customer/', create_customer, name='create_customer'),
    path('list_customer/', list_customer, name='list_customer'),
    path('edit_customer/<str:pk>', edit_customer, name='edit_customer'),
    path('list_customer_id/<str:pk>', list_customer_id, name='list_customer_id'),
    path('customer_with_greatrisk/', customer_with_greatrisk, name='customer_with_greatrisk'),
]