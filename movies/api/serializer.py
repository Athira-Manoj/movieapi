from rest_framework import serializers
from .models import Movies

class MovieSerializer(serializers.Serializer):
    name=serializers.CharField()
    year=serializers.IntegerField()
    director=serializers.CharField()
    genre=serializers.CharField()
    
    
class MovieModelSer(serializers.ModelSerializer):
    class Meta:
        model=Movies
        fields="__all__"