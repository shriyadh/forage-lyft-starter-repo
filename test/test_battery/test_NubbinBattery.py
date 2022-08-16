import unittest
from Battery.NubbinBattery import NubbinBattery
from datetime import date


class TestNubbinBattery(unittest.TestCase):
    def test_needs_services(self):
        today = date.fromisoformat("2020-05-15")
        last_service_date = date.fromisoformat("2015-05-25")

        battery = NubbinBattery(today, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_not_need_service(self):
        today = date.fromisoformat("2020-05-15")
        last_service_date = date.fromisoformat("2019-05-25")

        battery = NubbinBattery(today, last_service_date)
        self.assertFalse(battery.needs_service())
