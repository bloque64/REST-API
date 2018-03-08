from django.forms import widgets
from rest_framework import serializers
from servicios.models import  Steemit
from servicios.models import Publicacion
    
    


class PublicacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publicacion
        fields = ('id', 'autor', 'title', 'cuerpo', 'evaluado' ,  'formateado', 'curado')
        
class SteemitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Steemit
        fields = ('id',  'autor', 'title', 'cuerpo', 'votado' ,'publicado' , 'publicado_fecha')
