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
            self.__get_module().cancel_reservation(self.test_key, 'invalid type')

    def test_cancel_invalid_receiver_error_message(self):
        with self.assertRaisesMessage(gabia_sms.SMSModuleException,
                                      'Please check parameters type!'):
            self.__get_module().cancel_reservation(self.test_key, 'sms', int)
            self.__get_module().cancel_reservation(self.test_key, 'sms', dict)

    def test_cancel_invalid_receiver_regex_error_message(self):
        with self.assertRaisesMessage(gabia_sms.SMSModuleException,
                                      'Please check phone number!'):
            self.__get_module().cancel_reservation(self.test_key, 'sms', '01500000000')
            self.__get_module().cancel_reservation(self.test_key, 'sms', '0101234')
            self.__get_module().cancel_reservation(self.test_key, 'sms', '010123456')
