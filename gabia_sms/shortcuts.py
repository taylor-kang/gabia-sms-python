from .core import GabiaSMS


def send(message, receiver, title='SEND', sms_type='sms', scheduled_time='0', *args, **kwargs):
    """
    Shortcut function for send SMS\n
    :param message: Message
    :param receiver: Receive Phone number
    :param title: SMS TITLE(DEFAULT VALUE: 'SEND') : Used where the sms_type is 'lms'
    :param sms_type: ref KNOWN_SMS_TYPES: default is sms
    :param scheduled_time: default 0: send immediately or '%Y-%M-%D %h:%m:%s'
    :return Key of sent SMS
    """
    return GabiaSMS().send(message, receiver, title, sms_type, scheduled_time, *args, **kwargs)
