from django.conf import settings
from django.test import TestCase

import gabia_sms


class AppConfigTestCase(TestCase):

    @staticmethod
    def __set_empty_setting():
        module_settings = settings.GABIA_SMS_SETTINGS

        module_settings['SENDER'] = ''
        module_settings['API_ID'] = ''
        module_settings['API_KEY'] = ''

    @staticmethod
    def __set_default_test_setting():
        module_settings = settings.GABIA_SMS_SETTINGS

        module_settings['SENDER'] = '01000000000'
        module_settings['API_ID'] = 'test_api_id'
        module_settings['API_KEY'] = 'test_api_key'

    def test_empty_setting(self):
        AppConfigTestCase.__set_empty_setting()

        with self.assertRaises(gabia_sms.SMSModuleException):
            gabia_sms.GabiaSMS()

        AppConfigTestCase.__set_default_test_setting()
