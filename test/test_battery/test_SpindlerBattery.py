import unittest
from datetime import date
from Battery.SpindlerBattery import SpindlerBattery


class TestSpindlerBattery(unittest.TestCase):
    def test_needs_services(self):
        today = date.fromisoformat("2020-01-15")
        last_service_date = date.fromisoformat("2016-05-25")

        battery = SpindlerBattery(today, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_not_need_service(self):
        today = date.fromisoformat("2020-05-15")
        last_service_date = date.fromisoformat("2018-05-25")

        battery = SpindlerBattery(today, last_service_date)
        self.assertFalse(battery.needs_service())