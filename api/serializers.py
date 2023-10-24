from rest_framework import serializers
from api.models import ProblemsHealth, Client

class ProblemHealthSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProblemsHealth
        fields = ('name_problem', 'rating')

    def validate_rating(self, value):
        if (value > 2 or value < 1):
            raise serializers.ValidationError(f'Erro de validação Rating deve ser 1 ou 2 e você enviou {value}')
        return value
class ClientSerializer(serializers.ModelSerializer):
    problem_health = ProblemHealthSerializer(many=True)  

    class Meta:
        model = Client
        exclude = ['date_create', 'data_update']
        
    
    def create(self, validated_data):
        problems_data = validated_data.pop('problem_health')
        client = Client.objects.create(**validated_data)

        for problem_data in problems_data:
            problem = ProblemsHealth.objects.create(**problem_data)
            client.problem_health.add(problem)

        return client
    

class ClientSerializerList(serializers.ModelSerializer):
    
    problem_health = ProblemHealthSerializer(many=True)

    class Meta:
        model = Client
        fields = '__all__'


class ClientSerializerUpdate(serializers.ModelSerializer):
    problem_health = ProblemHealthSerializer(many=True)

    class Meta:
        model = Client
        exclude = ['date_create', 'data_update'] 

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.birthday = validated_data.get('birthday', instance.birthday)
        instance.sex = validated_data.get('sex', instance.sex)

        problems_data = validated_data.get('problem_health', [])
        instance.problem_health.clear()  

        for problem_data in problems_data:
            problem = ProblemsHealth.objects.create(**problem_data)
            instance.problem_health.add(problem)

        instance.save()
        return instance

