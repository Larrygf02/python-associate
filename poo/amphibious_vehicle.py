from boat import Boat
from car import Car

class AmphibiousVehicle(Car, Boat):

    def __init__(self, engine='2', tires=[], distance_traveled=0, unit='miles'):
        super().__init__(engine, tires, distance_traveled, unit)
        self.boat_type = 'motor'
    
    def travel(self, land_distance=0, water_distance=0):
        super().voyage(water_distance)
        super().drive(land_distance)