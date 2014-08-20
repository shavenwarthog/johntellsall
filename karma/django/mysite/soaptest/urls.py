from django.conf.urls import patterns, include, url
from soaptest import views

urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),

    (r'^hello/$', views.hello_world_service),
    (r'^hello/service.wsdl$', views.hello_world_service),
)

