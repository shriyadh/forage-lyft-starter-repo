from Battery.Battery import Battery


class NubbinBattery(Battery):
    def __init__(self, current_date, last_service_date):
        self.current_date = current_date
        self.last_service_date = last_service_date

    def needs_service(self):
        service_due_date =self.add_year(self.last_service_date,4)

        if service_due_date < self.current_date:
            return True
        return False

    def add_year(self, original_date, years_to_add):
        result = original_date.replace(year=original_date.year + years_to_add)
        return result