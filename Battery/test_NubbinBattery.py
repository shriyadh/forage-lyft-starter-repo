import unittest
from NubbinBattery import NubbinBattery


class TestNubbinBattery(unittest.TestCase):
    def test_needs_services(self):
        today = 2022
        last_service_date = 2006

        battery = NubbinBattery(today, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_not_need_service(self):
        today = 2022
        last_service_date = 2021

        battery = NubbinBattery(today, last_service_date)
        self.assertFalse(battery.needs_service())