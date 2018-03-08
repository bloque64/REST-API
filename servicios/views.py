from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
#from servicios.models import Publicacion
from servicios.serializers import SteemitSerializer
from servicios.serializers import PublicacionSerializer


from servicios.models import  Steemit
from servicios.models import Publicacion
#from servicios.serializers import Publicacion, Steemit
from rest_framework import generics

from django.contrib.auth import authenticate
from rest_framework.status import HTTP_401_UNAUTHORIZED
from rest_framework.authtoken.models import Token



class PublicacionList(generics.ListCreateAPIView):
    queryset = Publicacion.objects.all()
    serializer_class = PublicacionSerializer


class PublicacionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Publicacion.objects.all()
    serializer_class = PublicacionSerializer




class SteemitList(generics.ListCreateAPIView):
    queryset = Steemit.objects.all()
    #print "FUNCIONA queryset SteemitList"
    #print "FUNCIONA queryset SteemitList", queryset
    serializer_class = SteemitSerializer


class SteemitDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Steemit.objects.all()
    serializer_class = SteemitSerializer

