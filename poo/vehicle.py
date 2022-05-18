class Vehicle():

    #default_tire = 'tire'
    def __init__(self, distance_traveled=0, unit='miles'):
        self.distance_traveled = distance_traveled
        self.unit = unit
        pass

    #@classmethod #this is a simple way that you can create custom constructor
    #def bicycle(cls, tires=None):
    #    if not tires:
    #        tires = [cls.default_tire, cls.default_tire]
    #    return cls(None, tires)

    def description(self):
        message = f"A {self.__class__.__name__} vehicle that has traveled {self.distance_traveled} {self.unit}"
        return message
