from django.test import TestCase

import gabia_sms


class SendTestCase(TestCase):

    test_message = 'Test Message'
    test_receiver = '01000000000'

    def test_invalid_send_type(self):
        module = gabia_sms.SingletonGabiaSMS()

        with self.assertRaises(gabia_sms.SMSModuleException):
            module.send(self.test_message, self.test_receiver,
                        sms_type='invalid')

    def test_invalid_sent_type_error_message(self):
        module = gabia_sms.SingletonGabiaSMS()

        with self.assertRaisesMessage(gabia_sms.SMSModuleException,
                                      'Please check sms type!'):
            module.send(self.test_message, self.test_receiver,
                        sms_type='invalid')
