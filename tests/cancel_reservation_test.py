from django.test import TestCase

import gabia_sms


class SendTestCase(TestCase):

    test_message = 'Test Message'
    test_receiver = '01000000000'
    test_key = '1523688246'

    @classmethod
    def __get_module(cls):
        return gabia_sms.SingletonGabiaSMS()

    def test_cancel_invalid_sent_type_error_message(self):
        with self.assertRaisesMessage(gabia_sms.SMSModuleException,
                                      'Please check sms type!'):
            module = self.__get_module()

            module.cancel_reservation(self.test_key, 'invalid type')

    def test_cancel_invalid_receiver_error_message(self):
        with self.assertRaisesMessage(gabia_sms.SMSModuleException,
                                      'Please check parameters type!'):
            module = self.__get_module()

            module.cancel_reservation(self.test_key, 'sms', int)
            module.cancel_reservation(self.test_key, 'sms', dict)

    def test_cancel_invalid_receiver_regex_error_message(self):
        with self.assertRaisesMessage(gabia_sms.SMSModuleException,
                                      'Please check phone number!'):
            module = self.__get_module()

            module.cancel_reservation(self.test_key, 'sms', '01500000000')
            module.cancel_reservation(self.test_key, 'sms', '0101234')
            module.cancel_reservation(self.test_key, 'sms', '010123456')

    def test_cancel_invalid_receivers_regex_error_message(self):
        with self.assertRaisesMessage(gabia_sms.SMSModuleException,
                                      'Please check phone number!'):
            module = self.__get_module()

            module.cancel_reservation(
                self.test_key, 'sms', ['01500000000', self.test_receiver]
            )
            module.cancel_reservation(
                self.test_key, 'sms', ['0101234', self.test_receiver]
            )
            module.cancel_reservation(
                self.test_key, 'sms', ['010123456', self.test_receiver]
            )
