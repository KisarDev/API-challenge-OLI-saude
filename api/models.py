from django.db import models
from django.utils import timezone

class ProblemsHealth(models.Model):
    name_problem = models.CharField(max_length=30)
    rating = models.IntegerField()

    def __str__(self):
        return self.name_problem
    
class Client(models.Model):
    name = models.CharField(max_length=50)
    birthday = models.DateField()
    sex_choices = (
        ('M','Masculino'),
        ('F','Feminino'),
        ('O','Outro')
    )
    sex = models.CharField(max_length=1, choices=sex_choices)
    problem_health = models.ManyToManyField('ProblemsHealth', related_name='problem')
    date_create = models.DateTimeField()
    data_update = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.name
