from .core import GabiaSMS


def send(receiver, message, sms_type='sms', scheduled_time='0', *args, **kwargs):
    """
    Shortcut function for send SMS\n
    :param receiver: Receive Phone number
    :param message: Message
    :param sms_type: ref KNOWN_SMS_TYPES: default is sms
    :param scheduled_time: default 0: send immediately or '%Y-%M-%D %h:%m:%s'
    """
    GabiaSMS().send(receiver, message, sms_type, scheduled_time, *args, **kwargs)
