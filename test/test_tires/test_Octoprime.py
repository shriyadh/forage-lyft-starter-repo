import unittest
from Tires.OctoprimeTires import OctoprimeTires


class TestOctoprimeTires(unittest.TestCase):
    def test_needs_service(self):
        tire_wear = [0.9, 0.7, 0.9, 0.7]
        tires = OctoprimeTires(tire_wear)
        self.assertTrue(tires.needs_service())

    def test_not_need_service(self):
        tire_wear = [0.1, 0.2, 0.3, 0.4]
        tires = OctoprimeTires(tire_wear)
        self.assertFalse(tires.needs_service())