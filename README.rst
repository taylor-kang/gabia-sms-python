Gabia SMS module for Django
~~~~~~~~~~~~~

Python 2 & 3 compatible

.. image:: https://travis-ci.org/hwshim0810/gabia-sms-Django.svg?branch=master
    :target: https://travis-ci.org/hwshim0810/gabia-sms-Django/
.. image:: https://coveralls.io/repos/github/hwshim0810/gabia-sms-Django/badge.svg?branch=master
    :target: https://coveralls.io/github/hwshim0810/gabia-sms-Django?branch=master

- Source code: `<https://github.com/hwshim0810/gabia-sms-Django>`_

Quickstart
----------

Send sms message to use shortcut function

.. sourcecode:: python

   >>> import gabia_sms
   >>>
   >>> try:
   >>>     gabia_sms.send(receiver='will receive phone number', message='message')
   >>> except SMSModuleException:
   >>>     print('SMS send failure')


Advanced usage
----------
Inherit SMS class, override post_sent_sms / before_send_sms

.. sourcecode:: python

   >>> import gabia_sms
   >>>
   >>> class AdvancedSMSModule(GabiaSMS):
   >>>
   >>> def post_sms_sent(self, param, *args, **kwargs):
   >>>    # ... Do what you need
   >>>
   >>> def before_send_sms(self, param, *args, **kwargs):
   >>>    # ... Do what you need
   >>>
   >>> AdvancedSMSModule.send(receiver='will receive phone number', message='message')

Dependencies
------------

- Python 2.7 or 3.4+
- Django 1.11+

Installation
------------

You can install the library directly from pypi using pip:

.. sourcecode:: shell

    $ pip install gabia-sms-Django

Edit your settings.py file:

.. sourcecode:: python

    >>> GABIA_SMS_SETTINGS = {
    >>>     'SENDER': 'YOUR NUMBER',
    >>>     'API_ID': 'YOUR API ID,
    >>>     'API_KEY': 'YOUR API KEY'
    >>> }

Contributors
------------

See https://github.com/hwshim0810/gabia-sms-Django/graphs/contributors