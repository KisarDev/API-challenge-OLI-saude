from django.urls import path
from api.views import big_health_risk, client_edit, criar, get_client_id, order

urlpatterns = [
    path('create/', criar, name='create'),
    path('order/', order, name='order'),
    path('edit/<str:pk>', client_edit, name='edit'),
    path('get/<str:pk>', get_client_id, name='get'),
    path('most_risk/', big_health_risk, name='most_risk'),
]