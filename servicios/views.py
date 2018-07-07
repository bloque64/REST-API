from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
#from servicios.models import Publicacion

from servicios.serializers import ArticleSerializer
from servicios.serializers import UserSerializer



from servicios.models import Article
from servicios.models import User
#from servicios.serializers import Publicacion, Steemit
from rest_framework import generics

#from django.contrib.auth import authenticate
#from rest_framework.status import HTTP_401_UNAUTHORIZED
#from rest_framework.authtoken.models import Token



class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer



class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    #print "FUNCIONA queryset SteemitList"
    #print "FUNCIONA queryset SteemitList", queryset
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
