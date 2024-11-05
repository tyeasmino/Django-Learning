from django.db import models
from locations.models import Location
from diagnostic_center.models import Diagnostic_Center
from django.contrib.auth.models import User



# Create your models here.
class Investigation(models.Model):
    patient_name = models.CharField(max_length=100)
    age = models.IntegerField()
    test_details = models.CharField(max_length=100)    
    location = models.ForeignKey(Location, on_delete=models.DO_NOTHING)  
    diagnostic_center = models.ForeignKey(Diagnostic_Center, on_delete=models.DO_NOTHING) 
    marketing_executive = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=None)
    rate = models.IntegerField()
 
    payment_options = [
        ('P', 'Paid'), 
        ('D', 'Due')
    ]
    payment_status = models.CharField(max_length=2, choices=payment_options, default='D')


    def __str__(self):
        return f'{self.location} - {self.diagnostic_center} - {self.patient_name}'
    