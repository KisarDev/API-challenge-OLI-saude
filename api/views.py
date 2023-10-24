from .serializers import ClientSerializer, ClientSerializerList, ClientSerializerUpdate
from rest_framework.response import Response
from api.models import Client
from django.http import JsonResponse
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
import logging
import math

logger = logging.getLogger(__name__)

@swagger_auto_schema(method='post', request_body=ClientSerializer)
@api_view(['POST'])
def create_customer(request):
    """
    - Esse 'Endpoint' faz o cadastro de um cliente
    juntamente com seu problema de saúde e grau da doença no banco de dados.
    """
    if request.method != 'POST':
        return JsonResponse({'error': 'Método não permitido'}, status=405) 
    
    serializer = ClientSerializer(data=request.data)
    


    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201) 
    else:
        return JsonResponse(serializer.errors, status=400,)  


@api_view(['GET'])
def list_customer(request):
    """
    - Esse 'Endpoint' lista todos os clientes cadastrados.
    """
    if request.method != 'GET':
        return JsonResponse({'error': 'Método não permitido'}, status=405)
    
    client = Client.objects.all()
    serializer = ClientSerializerList(client, many=True)
    return Response(serializer.data)

@swagger_auto_schema(method='put', request_body=ClientSerializerUpdate)
@api_view(['PUT'])
def edit_customer(request, pk):
    """
    - Esse 'Endpoint' permite editar um cliente pelo ID.
    """
    if request.method != 'PUT':
        return JsonResponse({'error': 'Método não permitido'}, status=405)
    client = Client.objects.get(id=pk)
    
    serializer = ClientSerializerUpdate(client, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def list_customer_id(request, pk):
    """
    - Esse 'Endpoint' permite editar um cliente pelo ID.
    """
    if request.method != 'GET':
        return JsonResponse({'error': 'Método não permitido'}, status=405)
    client = Client.objects.get(id=pk)
    serializer = ClientSerializerList(client)

    return Response(serializer.data)

@api_view(['GET'])
def customer_with_greatrisk(request):
    """
    - Esse 'Endpoint' permite listar os 10 clientes com maior risco de saude.
    - Usando como base o calcula na formula score = (1 / (1 + e^(-2.8 + sd))) * 100
    """
    client = Client.objects.all()
    serializer = ClientSerializerList(client, many=True)
    serializer = serializer.data
    list_customer_and_problem = []
    ratings = {}
    for objeto in serializer:
        list_customer_and_problem += [objeto['name'],objeto['problem_health']]
        
    for index in range(0, len(list_customer_and_problem), 2):
        customer = list_customer_and_problem[index]  
        sicks = list_customer_and_problem[index + 1]  
    
    
        total_ratings = sum(problem['rating'] for problem in sicks)
    
    
        if customer in ratings:
            ratings[customer] += total_ratings
        else:
            ratings[customer] = total_ratings

    customer_score = []
    list_rating = []

    for customer, rating in ratings.items():
        score = (1 / (1 + math.exp(-(-2.8 + rating)))) * 100
        list_rating += [score]
        customer_score += [customer, score]

    pairs_customer_and_score = [(customer_score[i], customer_score[i+1]) for i in range(0, len(customer_score), 2)]

    sorted_pairs = sorted(pairs_customer_and_score, key=lambda x: x[1], reverse=True)

    most_10_risk = [i[0] for i in sorted_pairs[:10]]

    print(pairs_customer_and_score)
        
    return Response(most_10_risk)

    