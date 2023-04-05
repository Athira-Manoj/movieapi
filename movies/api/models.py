from django.db import models

# Create your models here.

movies=[
    {"id":1,"name":"Sphadikam","year":1996,"Director":"Bharathan","genre":"drama"},
    {"id":2,"name":"drishyam","year":2013,"Director":"jithu Jospeph","genre":"thriller"},
    {"id":3,"name":"lucifer","year":2019,"Director":"Prithviraj","genre":"drama"},
    {"id":4,"name":"thor","year":2017,"Director":"taika","genre":"drama"},
    {"id":5,"name":"iron man","year":2008,"Director":"jon faureau","genre":"action"},
    {"id":6,"name":"minnaram","year":1994,"Director":"priyadharshan","genre":"drama"},
]

class Movies(models.Model):
    name=models.CharField(max_length=100)
    year=models.IntegerField()
    director=models.CharField(max_length=100)
    genre=models.CharField(max_length=100)
    
    
    
    


