class Vehicle():
    
    def __init__(self, engine, tires):
        self.engine = engine
        self.tires = tires
        pass

    def description(self):
        print(f"a vehicle with an {self.engine} engine, and {self.tires} tires")
