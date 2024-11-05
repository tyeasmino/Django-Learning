from django.db import models
from locations.models import Location

# Create your models here.
class Profiles(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=50)
    phone_no = models.CharField(max_length=11)
    salary = models.IntegerField()
    target_amount = models.IntegerField() 
    location = models.OneToOneField(Location, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return f'{self.location} - {self.name}' 
    