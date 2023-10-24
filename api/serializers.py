from rest_framework import serializers
from api.models import ProblemsHealth, Client

class ProblemHealthSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProblemsHealth
        fields = ('name_problem', 'rating')

    def validate_rating(self, value):
        if (value > 2) or (value < 1):
            print("ERRO")
            raise serializers.ValidationError("Precisa ser 1 ou 2")
        return value

class ClientSerializer(serializers.ModelSerializer):
    problem_health = ProblemHealthSerializer(many=True)  

    class Meta:
        model = Client
        fields = '__all__'
    # def validate_sex(self, value):
    #     if value != "M" or value != "F" or value != "O":
    #         raise serializers.ValidationError("ERRO")
    def create(self, validated_data):
        problems_data = validated_data.pop('problem_health')
        client = Client.objects.create(**validated_data)

        for problem_data in problems_data:
            problem = ProblemsHealth.objects.create(**problem_data)
            client.problem_health.add(problem)

        return client
    

class ClientSerializerOrder(serializers.ModelSerializer):
    problem_health = ProblemHealthSerializer(many=True)

    class Meta:
        model = Client
        fields = '__all__'

# CLASSE USADA PARA DEFINIR A FUNÇÃO DE ATUALIZAR O BANCO 
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
        instance.problem_health.clear()  # Remove todas as associações ManyToMany existentes

        for problem_data in problems_data:
            problem = ProblemsHealth.objects.create(**problem_data)
            instance.problem_health.add(problem)

        instance.save()
        return instance

