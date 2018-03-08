from django.conf.urls import url, include
from servicios.views import PublicacionList, PublicacionDetail, SteemitList, SteemitDetail
from rest_framework.urlpatterns import format_suffix_patterns
from servicios.api import PublicacionResource
from tastypie.api import Api

#from services.api import PublicacionResource, PostSteemitResource

v1_api = Api(api_name='v1')
v1_api.register(PublicacionResource())
## PODEMOS AGREGAR OTRA
#v1_api.register(PostSteemitResource())

urlpatterns = [
                
                url(r'^publicaciones/$', PublicacionList.as_view()),
                url(r'^publicaciones/(?P<pk>[0-9]+)/$', PublicacionDetail.as_view()),
                
                
                url(r'^steemit/$', SteemitList.as_view()),
                url(r'^steemit/(?P<pk>[0-9]+)/$', SteemitDetail.as_view()),
                
                url(r'^api/', include(v1_api.urls)),
]
urlpatterns = format_suffix_patterns(urlpatterns)

