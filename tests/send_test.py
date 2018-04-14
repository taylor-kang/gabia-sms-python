from unittest.mock import MagicMock

from django.test import TestCase

import gabia_sms


class SendTestCase(TestCase):

    test_message = 'Test Message'
    test_receiver = '01000000000'
    test_key = '1523688246'

    @classmethod
    def __get_module(cls):
        return gabia_sms.SingletonGabiaSMS()

    def test_invalid_sent_type_error_message(self):
        with self.assertRaisesMessage(gabia_sms.SMSModuleException,
                                      'Please check sms type!'):
            self.__get_module().send(self.test_message, self.test_receiver,
                                     sms_type='invalid')

    def test_empty_message_error_message(self):
        with self.assertRaisesMessage(gabia_sms.SMSModuleException,
                                      'Please check required parameters!'):
            self.__get_module().send('', self.test_receiver)

    def test_empty_receiver_error_message(self):
        with self.assertRaisesMessage(gabia_sms.SMSModuleException,
                                      'Please check required parameters!'):
            self.__get_module().send(self.test_message, '')

    def test_invalid_message_type_error_message(self):
        with self.assertRaisesMessage(gabia_sms.SMSModuleException,
                                      'Please check parameters type!'):
            self.__get_module().send(1234, self.test_receiver)

    def test_invalid_receiver_type_error_message(self):
        with self.assertRaisesMessage(gabia_sms.SMSModuleException,
                                      'Please check parameters type!'):
            self.__get_module().send(self.test_message, 1000000000)

    def test_invalid_receiver_regex_error_message(self):
        with self.assertRaisesMessage(gabia_sms.SMSModuleException,
                                      'Please check phone number!'):
            module = self.__get_module()

            module.send(self.test_message, '01500000000')
            module.send(self.test_message, '0101234')
            module.send(self.test_message, '010123456')

    def test_received_invalid_auth_code_after_invalid_auth_request(self):
        module = self.__get_module()
        module.send = MagicMock()
        module.send.return_value = self.test_key, gabia_sms.codes.INVALID_AUTH_REQUEST_CODE

        _, code = module.send(self.test_message, self.test_receiver)

        self.assertEqual(code, gabia_sms.codes.INVALID_AUTH_REQUEST_CODE)
