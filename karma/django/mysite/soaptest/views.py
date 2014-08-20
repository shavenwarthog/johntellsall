from soaptest.soaplib_handler import (
    DjangoSoapApp, soapmethod, soap_types
    )
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return HttpResponse('howdy')


class SmsGatewayService(DjangoSoapApp):

    __tns__ = 'http://mismsgw01.milano.ea.it/soap'

    @soapmethod(
        soap_types.String, 
        soap_types.String, 
        soap_types.String, 
        soap_types.Integer,
        soap_types.Boolean, 
        soap_types.Boolean, 
        soap_types.String, 
        _returns=soap_types.Any
    )
    def sendSms(
        self, 
        sendTo, 
        numSender,
        senderDescription,
        timeToLive,
        isDelivered,
        isStatistics,
        messageText
    ):

        retCode = '<retCode>OK</retCode>'

        return retCode

    def index(self):
        return '<retCode>OK</retCode>'

sms_gateway_service = csrf_exempt(SmsGatewayService())


class HelloWorldService(DjangoSoapApp):

    __tns__ = 'http://my.namespace.org/soap/'

    @soapmethod(soap_types.String, soap_types.Integer, _returns=soap_types.Array(soap_types.String))
    def say_hello(self, name, times):
        results = []
        for i in range(0, times):
            results.append('Hello, %s'%name)
        return results

hello_world_service = HelloWorldService()
