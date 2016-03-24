from django.conf import settings
from appconf import AppConf


class authorizeConf(AppConf):

    TEST_URL = False

    class Meta:
        prefix = 'authorize'
