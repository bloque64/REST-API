# services/api.py

from tastypie.resources import ModelResource
from servicios.models import Publicacion

from tastypie.authentication import BasicAuthentication


class PublicacionResource(ModelResource):
    class Meta:
        queryset = Publicacion.objects.all()
        resource_name = 'Publicacion'
        allowed_methods = ['get', 'post', 'put']
        authentication = BasicAuthentication()
        
        