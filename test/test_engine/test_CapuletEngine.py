import unittest

from Engine.CapuletEngine import CapuletEngine


class TestCapuletEngine(unittest.TestCase):
    def test_needs_service(self):
        current_mileage = 30500
        last_service_mileage = 10

        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_not_needs_service(self):
        current_mileage = 30000
        last_service_mileage = 20000

        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())