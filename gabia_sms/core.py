from __future__ import with_statement

import hashlib
import re

from django.conf import settings
from django.utils import timezone

from .exceptions import SMSModuleException
from .formats import REQUEST_SMS_XML_FORMAT
from .parser import get_result_code
from .utils import escape_xml_string, get_nonce


try:
    import xmlrpc.client as xmlrpc_lib
except ImportError:
    import xmlrpclib as xmlrpc_lib


PHONE_NUMBER_REGEX = '01[0|1|6|7|8|9]{1}[0-9]{7,8}'

MISSING_SETTING = (
    'GABIA_SMS_SETTINGS {setting} is required'
)
REQUIRED_SETTINGS = ('API_ID', 'API_KEY', 'SENDER')
KNOWN_SMS_TYPES = ('sms', 'lms', 'multi_sms', 'multi_lms')
SUCCESS_CODE = '0000'


class GabiaSMS:

    __API_URL = 'http://sms.gabia.com/api'
    __MODULE_SETTINGS_NAME = 'GABIA_SMS_SETTINGS'

    def __init__(self):
        self.__settings = self.__get_module_settings()
        self.__validate_settings()

    def __get_module_settings(self):
        module_settings = getattr(settings, self.__MODULE_SETTINGS_NAME, {})

        for setting_key in REQUIRED_SETTINGS:
            module_settings.setdefault(setting_key, None)

        return module_settings

    def __validate_settings(self):
        for key, value in self.__settings.items():
            if not value:
                raise SMSModuleException(MISSING_SETTING.format(setting=key))

    def __validate_required_params(self, message, receiver):
        if not (message and receiver):
            raise SMSModuleException('Please check required parameters!')
        elif not isinstance(message, str) or not isinstance(receiver, str):
            raise SMSModuleException('Please check parameters type!')
        elif not re.compile(PHONE_NUMBER_REGEX).search(receiver):
            raise SMSModuleException('Please check phone number!')

    def __get_md5_access_token(self):
        nonce = get_nonce()
        return nonce + hashlib.md5(
            (nonce + self.__settings['API_KEY']).encode()
        ).hexdigest()

    def post_sent_sms(self, *args, **kwargs):
        """
        Post sent sms task\n
        Do what you need to override
        """
        pass

    def before_send_sms(self, *args, **kwargs):
        """
        Before send sms task\n
        Do what you need to override
        """
        pass

    def __get_sms_param(self, message, receiver, scheduled_time,
                        sms_type='sms', title='SEND'):

        self.__validate_required_params(message, receiver)

        return {
            'sender': self.__settings['SENDER'],
            'sms_type': sms_type,
            'message': escape_xml_string(message),
            'receiver': receiver,
            'title': escape_xml_string(title),
            'scheduled_time': scheduled_time,
            'key': int(timezone.now().timestamp())
        }

    def send(self, receiver, message,
             sms_type='sms', scheduled_time='0', *args, **kwargs):
        """
        Use for send SMS\n
        :param receiver: Receive Phone number
        :param message: Message
        :param sms_type: ref KNOWN_SMS_TYPES: default is sms
        :param scheduled_time: default 0: send immediately or '%Y-%M-%D %h:%m:%s'
        """
        if sms_type not in KNOWN_SMS_TYPES:
            raise SMSModuleException('Please check sms type!')

        self.__send_single(
            self.__get_sms_param(message, receiver, scheduled_time),
            *args,
            **kwargs
        )

    def __send_single(self, param, *args, **kwargs):

        with xmlrpc_lib.ServerProxy(self.__API_URL) as proxy:
            try:
                self.before_send_sms(param, *args, **kwargs)

                response = proxy.gabiasms(
                    REQUEST_SMS_XML_FORMAT.format(
                        api_id=self.__settings['API_ID'],
                        access_token=self.__get_md5_access_token(),
                        sms_type=param['sms_type'],
                        key=param['key'],
                        title=param['title'],
                        message=param['message'],
                        sender=param['sender'],
                        receiver=param['receiver'],
                        scheduled_time=param['scheduled_time']
                    )
                )
                result_code = get_result_code(response)

                if result_code != SUCCESS_CODE:
                    import logging
                    logging.getLogger(__name__).debug(result_code)

                self.post_sent_sms(param, *args, **kwargs)

            except xmlrpc_lib.Error as e:
                import logging
                logging.getLogger(__name__).error(e)
                raise SMSModuleException('Bad request. Please check api docs')
