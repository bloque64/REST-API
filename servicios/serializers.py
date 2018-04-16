from django.forms import widgets
from rest_framework import serializers
from servicios.models import  Steemit
from servicios.models import Publicacion




class PublicacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publicacion
        fields = ('id', 'autor', 'token', 'title', 'cuerpo', 'image', 'evaluado',  'formateado', 'curado')

class SteemitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Steemit
        fields = ('id', 'autor' , 'title', 'cuerpo', 'image', 'votado', 'publicado', 'publicado_fecha')
