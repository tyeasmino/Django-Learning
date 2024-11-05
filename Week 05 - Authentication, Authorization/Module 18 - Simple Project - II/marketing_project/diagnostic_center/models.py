from django.db import models
from locations.models import Location



# Create your models here.
class Diagnostic_Center(models.Model):
    name = models.CharField(max_length=50)
    location = models.ForeignKey(Location, on_delete=models.DO_NOTHING) 
    
    def __str__(self):
        return f"{self.location} - {self.name}" 
    