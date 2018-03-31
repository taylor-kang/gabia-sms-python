from .core import SingletonGabiaSMS


def send(message, receiver,
         title='SEND', sms_type='sms', scheduled_time='0', *args, **kwargs):
    """
    Shortcut function for send SMS\n
    :param message: Message
    :param receiver: Receive Phone number:
           if 'multi_sms' or 'multi_lms' receiver type is list or set
    :param title: SMS TITLE: Used where the sms_type is 'lms' or 'multi_lms'
    :param sms_type: ['sms', 'lms', 'multi_sms', 'multi_lms'] : default value is 'sms'
    :param scheduled_time: default 0: send immediately or '%Y-%M-%D %h:%m:%s'
    :return Key of sent SMS
    """
    return SingletonGabiaSMS().send(message, receiver, title,
                                    sms_type, scheduled_time, *args, **kwargs)


def get_send_result(key):
    """
    :param key: The key to lookup
    :return: Result code received by key
    """
    return SingletonGabiaSMS().get_send_result(key)
