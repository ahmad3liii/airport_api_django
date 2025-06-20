from django.db import models

# Create your models here.
class Airport(models.Model):
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=200)
    capacityOfAirplans=models.IntegerField(default=0)
    capacityOfPassengers=models.IntegerField(default=0)
    evaluation=models.IntegerField(default=0)
    def __str__(self):
        return self.name
