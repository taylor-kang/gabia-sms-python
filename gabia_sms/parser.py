from xml.etree.ElementTree import fromstring

from .exceptions import SMSModuleException


def get_result_code(response):
    root = fromstring(response)
    code = root.find('code')

    if code is None:
        raise SMSModuleException('Bad request. Please check api docs')

    return code.text
