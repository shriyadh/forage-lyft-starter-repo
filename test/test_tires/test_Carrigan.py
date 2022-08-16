import unittest
from Tires.CarriganTires import CarriganTires


class TestCarriganTires(unittest.TestCase):
    def test_needs_service(self):
        tire_wear = [0.9, 0.6, 0.7, 0.9]
        tires = CarriganTires(tire_wear)
        self.assertTrue(tires.needs_service())

    def test_not_need_service(self):
        tire_wear = [0.1, 0.1, 0.1, 0.1]
        tires = CarriganTires(tire_wear)
        self.assertFalse(tires.needs_service())