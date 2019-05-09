# -*- coding: utf-8 -*-
from __future__ import absolute_import

from pkg_resources import get_distribution

from .core import (
    GabiaSMS,
    SingletonGabiaSMS
)
from . import codes
from .exceptions import SMSModuleException
from .shortcuts import (
    send,
    get_send_result,
    cancel_reservation
)

__version__ = get_distribution('gabia-sms-python').version

__all__ = (
    'GabiaSMS',
    'SingletonGabiaSMS',
    'SMSModuleException',
    'send',
    'get_send_result',
    'cancel_reservation',
    'codes',
    'configure'
)
