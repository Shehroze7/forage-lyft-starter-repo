from abc import ABC

from car import Car

class SpindlerBattery(ABC, car):
     self.last_service_date = last_service_date
    self.current_date = current_date


def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 3)
        if service_threshold_date < datetime.today().date() or self.battery_should_be_serviced():
            return True
        else:
            return False
        pass