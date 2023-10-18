from django.db import models
from django.utils import timezone

class ProblemsHealth(models.Model):
    name_problem = models.CharField(max_length=30)
    rating = models.IntegerField()

    def __str__(self) -> str:
        return self.name_problem
    
class Client(models.Model):
    name = models.CharField(max_length=50)
    birthday = models.DateField()
    sex = models.CharField(max_length=1)
    problem_health = models.ManyToManyField(ProblemsHealth, unique=False)
    date_create = models.DateTimeField(default=timezone.now)
    data_update = models.DateTimeField(default=timezone.now)



