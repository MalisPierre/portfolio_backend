from django.test import TestCase

class DjangoBasicTestCase(TestCase):
    def setUp(self):
        pass

    def test_basic_stuff(self):
        self.assertEqual(True, True)