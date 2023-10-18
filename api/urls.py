from django.urls import path
from api.views import criar

urlpatterns = [
    path('create/', criar, name='create'),
]