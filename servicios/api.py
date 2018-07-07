# services/api.py

from tastypie.resources import ModelResource
from servicios.models import Article

from tastypie.authentication import BasicAuthentication


class ArticleResource(ModelResource):
    class Meta:
        queryset = Article.objects.all()
        resource_name = 'Article'
        allowed_methods = ['get', 'post', 'put']
        #authentication = BasicAuthentication()
