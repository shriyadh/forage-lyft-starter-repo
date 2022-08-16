import unittest

from WilloughbyEngine import WilloughbyEngine


class TestWilloughbyEngine(unittest.TestCase):
    def test_needs_service(self):
        current_mileage = 60050
        last_service_mileage = 10

        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_not_need_service(self):
        current_mileage = 60000
        last_service_mileage = 30000

        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())