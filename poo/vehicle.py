class Vehicle():

    default_tire = 'tire'
    def __init__(self, engine, tires):
        self.engine = engine
        self.tires = tires
        pass

    @classmethod #this is a simple way that you can create custom constructor
    def bicycle(cls, tires=None):
        if not tires:
            tires = [cls.default_tire, cls.default_tire]
        return cls(None, tires)

    def description(self):
        print(f"a vehicle with an {self.engine} engine, and {self.tires} tires")
