===========================
Gabia SMS module for Django
===========================

Python 2 & 3 compatible

.. image:: https://travis-ci.org/athenaslab/gabia-sms-Django.svg?branch=master
    :target: https://travis-ci.org/athenaslab/gabia-sms-Django/
.. image:: https://coveralls.io/repos/github/athenaslab/gabia-sms-Django/badge.svg?branch=master
    :target: https://coveralls.io/github/athenaslab/gabia-sms-Django?branch=master

- Source code: `<https://github.com/athenaslab/gabia-sms-Django>`_
- Distribution: `<https://pypi.python.org/pypi/gabia-sms-Django>`_
- Maintainer: `<https://github.com/hwshim0810>`_

Quickstart
----------

Send sms message to use shortcut function

.. code-block:: python

    import gabia_sms

    try:
        # Send single SMS
        gabia_sms.send(message='message', receiver='will receive phone number')

    except SMSModuleException:
        print('SMS send failure')

- SMS Types: ['sms', 'lms', 'multi_sms', 'multi_lms']
- Send function returning Tuple(Unique key, Result code)

More usage
----------

.. code-block:: python

    import gabia_sms

    try:
        # Reserve single SMS
        gabia_sms.send(
            message='message',
            receiver='will receive phone number',
            scheduled_time='2018-02-02 22:22:22'
        )

        # Send multiple SMS
        gabia_sms.send(message='message', receiver=['phone number', '...'])
        gabia_sms.send(message='message', receiver=('phone number', '...'))

        # Reserve multiple SMS
        gabia_sms.send(
            message='message',
            receiver=['phone number', '...'],
            scheduled_time='2018-02-02 22:22:22'
        )

        # Cancel reservation
        gabia_sms.cancel_reservation('Unique key', 'SMS type')

        # Request result code
        gabia_sms.get_send_result('Unique key')

    except SMSModuleException:
        print('SMS send failure')


Advanced usage
--------------
Inherit SMS class, override post_sent_sms / before_send_sms

.. code-block:: python

    import gabia_sms

    class AdvancedSMSModule(GabiaSMS):

      def post_sms_sent(self, param, *args, **kwargs):
         # ... Do what you need

      def before_send_sms(self, param, *args, **kwargs):
         # ... Do what you need

    AdvancedSMSModule.send(message='message', receiver='will receive phone number')


Dependencies
------------

- Python 2.7 or 3.4+
- Django 1.11+

Installation
------------

You can install the library directly from pypi using pip:

.. code-block:: shell

    $ pip install gabia-sms-Django

Edit your settings.py file:

.. code-block:: python

     GABIA_SMS_SETTINGS = {
         'SENDER': 'YOUR NUMBER',
         'API_ID': 'YOUR API ID,
         'API_KEY': 'YOUR API KEY'
     }

Contributors
------------

See https://github.com/hwshim0810/gabia-sms-Django/graphs/contributors
