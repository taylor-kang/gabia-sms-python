===========================
Gabia SMS module for Python
===========================

Python 2 & 3 compatible

- Source code: `<https://github.com/taylor-kang/gabia-sms-python>`_
- Distribution: `<https://pypi.org/project/gabia-sms-python>`_
- Maintainer: `<https://github.com/taylor-kang>`_

Installation
------------

You can install the library directly from pypi using pip:

.. code-block:: shell

    $ pip install gabia-sms-python

Dependencies
------------

- Python 2.7 or 3.4+

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

        # if not assign scheduled_time, send immediately
        gabia_sms.send(
            message='message',
            receiver='will receive phone number'
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

    class AdvancedSMSModule(gabia_sms.GabiaSMS):

      def post_sms_sent(self, param, *args, **kwargs):
         # ... Do what you need

      def before_send_sms(self, param, *args, **kwargs):
         # ... Do what you need

    AdvancedSMSModule.send(message='message', receiver='will receive phone number')

or Use SingletonClass

.. code-block:: python

    import gabia_sms

    class AdvancedSMSModule(gabia_sms.SingletonGabiaSMS):
        # ...
        pass

Acknowledgements
--------------
Thanks `<https://github.com/athenaslab/gabia-sms-Django>` for gabia-sms-Django version