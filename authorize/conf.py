from django.conf import settings
from appconf import AppConf


class authorizeConf(AppConf):

    TEST_URL = 'https://apitest.authorize.net/soap/v1/Service.asmx?WSDL'

    class Meta:
        prefix = 'authorize'
