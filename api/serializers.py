from rest_framework import serializers

from api.models import ProblemsHealth, Client

class ProblemsHealthSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProblemsHealth
        fields = '__all__'

        
class ClientSerializer(serializers.ModelSerializer):
    problems = ProblemsHealthSerializer(many=True)
    class Meta:
        model = Client
        fields = '__all__'

    def create(self, validated_data):
        problems_data = validated_data.pop('problems')
        pessoa = Client.objects.create(**validated_data)
        for problem_data in problems_data:
            ProblemsHealth.objects.create(pessoa=pessoa, **problem_data)
        return pessoa

