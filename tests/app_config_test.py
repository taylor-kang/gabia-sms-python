from django.test import TestCase

import gabia_sms


class AppConfigTestCase(TestCase):

    def test_empty_setting(self):

        with self.assertRaises(gabia_sms.SMSModuleException):
            gabia_sms.GabiaSMS()
