from rest_framework import serializers

from api.models import ProblemsHealth, Client

class ProblemsHealthSerializer(serializers.ModelSerializer):
    model = ProblemsHealth
    fields = '__all__'

        
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'
