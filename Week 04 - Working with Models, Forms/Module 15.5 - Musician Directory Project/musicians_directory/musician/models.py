from django.db import models

# Create your models here.
class MusiciansModel(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=11)
    
    instruments = [
        ('Violin', 'Violin'),
        ('Guitar', 'Guitar'),
        ('Drums', 'Drums'),
        ('Keyboard', 'Keyboard') 
    ]
    instrument_type = models.CharField(choices=instruments, max_length=8)


    def __str__(self):
        return f'{self.first_name} {self.last_name}'