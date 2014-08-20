from django.conf.urls import patterns, include, url
import soaptest

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^soaptest/', include('soaptest.urls')),
    url(r'^rpctest/', include('rpctest.urls')),
)
