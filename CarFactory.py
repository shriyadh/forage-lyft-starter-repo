from Engine import CapuletEngine
from Battery.NubbinBattery import NubbinBattery
from Battery.SpindlerBattery import SpindlerBattery
from Engine.SternmanEngine import SternmanEngine
from Engine.WilloughbyEngine import WilloughbyEngine
from Car import Car


class CarFactory:
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(current_date, last_service_date)
        battery = SpindlerBattery(current_mileage, last_service_mileage)
        return Car(engine, battery)

    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(current_date, last_service_date)
        battery = SpindlerBattery(current_mileage, last_service_mileage)
        return Car(engine, battery)

    def create_palindrome(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = SternmanEngine(current_date, last_service_date)
        battery = SpindlerBattery()
        return Car(engine, battery)

    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(current_date, last_service_date)
        battery = NubbinBattery(current_mileage, last_service_mileage)
        return Car(engine, battery)

    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(current_date, last_service_date)
        battery = NubbinBattery(current_mileage, last_service_mileage)
        return Car(engine, battery)
