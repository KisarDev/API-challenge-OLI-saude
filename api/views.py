from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from api.models import Client, ProblemsHealth
from .serializers import ClientSerializer, ClientSerializerOrder, ClientSerializerUpdate
from drf_yasg.utils import swagger_auto_schema
from rest_framework.exceptions import APIException
import logging
from django.http import JsonResponse
import math
logger = logging.getLogger(__name__)

@swagger_auto_schema(method='post', request_body=ClientSerializer)
@api_view(['POST'])
def criar(request):
    """
    Endpoint para criar um novo cliente.
    """
    if request.method != 'POST':
        logger.error('Método não permitido. Apenas requisições POST são aceitas.')
        return JsonResponse({'error': 'Método não permitido'}, status=405) 

    logger.debug('Requisição POST recebida com dados: %s', request.data)
    
    serializer = ClientSerializer(data=request.data)
    
    

    if serializer.is_valid():
        logger.debug('Dados válidos. Salvando o objeto Client no banco de dados.')
        serializer.save()
        return JsonResponse(serializer.data, status=201) 
    else:
        print(serializer.errors)
        logger.error('Dados inválidos: %s', serializer.errors)
        return JsonResponse(serializer.errors, status=400,)  


@api_view(['GET'])
def order(request):
    client = Client.objects.all()
    serializer = ClientSerializerOrder(client, many=True)
    return Response(serializer.data)

@swagger_auto_schema(method='put', request_body=ClientSerializerUpdate)
@api_view(['PUT'])
def client_edit(request, pk):
    client = Client.objects.get(id=pk)
    
    serializer = ClientSerializerUpdate(client, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_client_id(request, pk):
    client = Client.objects.get(id=pk)
    serializer = ClientSerializerOrder(client)

    return Response(serializer.data)

@api_view(['GET'])
def big_health_risk(request):  
    client = Client.objects.all()
    serializer = ClientSerializerOrder(client, many=True)
    serializer = serializer.data
    data = []
    ratings = {}
    for objeto in serializer:
        data += [objeto['name'],objeto['problem_health']]
        
    for i in range(0, len(data), 2):
        pessoa = data[i]  
        problemas = data[i + 1]  
    
    
        total_ratings = sum(problema['rating'] for problema in problemas)
    
    
        if pessoa in ratings:
            ratings[pessoa] += total_ratings
        else:
            ratings[pessoa] = total_ratings
    total_risk = []


    list_rating = []
    for pessoa, rating in ratings.items():
        score = (1 / (1 + math.exp(-(-2.8 + rating)))) * 100
        list_rating += [score]
        total_risk += [pessoa, score]
    
    ''''
    for i in range(len(total_risk)):
        if type(total_risk[i]) == float:
            most_score.append(total_risk[i])
    
    most_score = sorted(most_score, reverse=True)
    '''
        
    return Response(total_risk)

    