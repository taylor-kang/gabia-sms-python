from django.test import TestCase

import gabia_sms


class ClassTestCase(TestCase):

    def test_singleton_class(self):
        ins_one = gabia_sms.SingletonGabiaSMS()
        ins_two = gabia_sms.SingletonGabiaSMS()

        self.assertEqual(ins_one, ins_two)

    def test_general_class(self):
        ins_one = gabia_sms.GabiaSMS()
        ins_two = gabia_sms.GabiaSMS()

        self.assertNotEqual(ins_one, ins_two)
