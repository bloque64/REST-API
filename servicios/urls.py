from django.conf.urls import url, include
from servicios.views import ArticleList, ArticleDetail, UserList, UserDetail
from rest_framework.urlpatterns import format_suffix_patterns
from servicios.api import ArticleResource
from tastypie.api import Api

#from services.api import PublicacionResource, PostSteemitResource

v1_api = Api(api_name='v1')
v1_api.register(ArticleResource())
## PODEMOS AGREGAR OTRA
#v1_api.register(PostSteemitResource())

urlpatterns = [

                url(r'^articles/$', ArticleList.as_view()),
                url(r'^articles/(?P<pk>[0-9]+)/$', ArticleDetail.as_view()),

                url(r'^users/$', UserList.as_view()),
                url(r'^users/(?P<pk>[0-9]+)/$', UserDetail.as_view()),

                url(r'^api/', include(v1_api.urls)),
]
urlpatterns = format_suffix_patterns(urlpatterns)
