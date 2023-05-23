from tires import Tires
from typing import list

tire_wear_array=0
class  CarriganTires:
    def __init__(self, arr : list[tire_wear_array]):
        self.tire_wear_array = tire_wear_array



def needs_service(self):
    for wear_value in self.tire_wear_array:
        if sum(wear_value) >=3:
            print("Needs service")
        else:
            print("Does not need service")