from django.db import models
import psycopg2

# Create your models here.

class Worker(models.Model):
    name = models.CharField(max_length=20, blank= False)
    second_name = models.CharField(max_length=50, blank= False)
    salary = models.IntegerField (default=0)

    def __str__(self) -> str:
        return f'{self.name} {self.second_name}'