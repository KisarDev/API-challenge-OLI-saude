from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from api.models import ProblemsHealth
from .serializers import ClientSerializer
from drf_yasg.utils import swagger_auto_schema
from rest_framework.exceptions import APIException

@swagger_auto_schema(method='POST', request_body=ClientSerializer)
@api_view(['POST'])
def criar(request):
    """
    Exemplo da requisição
    """
    if request.method == 'GET':
        raise APIException(403, 'Sem acesso get')
    
    serializer = ClientSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)