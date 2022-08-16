from Battery import Battery


class SpindlerBattery(Battery):
    def __init__(self, current_date, last_service_date):
        self.current_date = current_date
        self.last_service_date = last_service_date

    def needs_service(self):
        service_due_date = self.last_service_date + 2

        if service_due_date < self.current_date:
            self.last_service_date = self.current_date
            return True
        return False
