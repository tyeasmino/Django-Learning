from django.db import models
from locations.models import Location

# Create your models here.
class Marketing_Executive(models.Model):
    name = models.CharField(max_length=100)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True, blank=True)   
    
    def __str__(self):
        return f'{self.name}'   
    

