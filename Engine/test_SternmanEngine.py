import unittest

from SternmanEngine import SternmanEngine


class TestSternmanEngine(unittest.TestCase):
    def test_needs_service(self):
        warning_light_is_on = True

        engine = SternmanEngine(warning_light_is_on)
        self.assertTrue(engine.needs_service())

    def test_not_need_service(self):
        warning_light_is_on = False

        engine = SternmanEngine(warning_light_is_on)
        self.assertFalse(engine.needs_service())
