from django.db import models
from musician.models import MusiciansModel

# Create your models here.
class AlbumsModel(models.Model):
    album_name = models.CharField(max_length=100)
    musician = models.ForeignKey(MusiciansModel, on_delete=models.CASCADE) 
    album_release_date = models.DateField(auto_now=True) 

    rates = [
        ('1', 'Rating 1'),
        ('2', 'Rating 2'),
        ('3', 'Rating 3'),
        ('4', 'Rating 4'),
        ('5', 'Rating 5'),
    ]
    album_rating = models.CharField(max_length=1, choices=rates)
    



    def __str__(self):
        return f'{self.album_name} - {self.musician.first_name}' 