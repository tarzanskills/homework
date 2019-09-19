class MotorBike:
    def __init__(self,colour, model, capacity, price, engine):
        self.colour = colour
        self.model = model
        self.capacity = capacity
        self.price = price
        self.engine = engine
    def ignition(self):
        print("starts the bike")
    def drive(self):
        print("drives the bike")
    def brake(self):
        print("halts the bike")

bike = MotorBike("Black", 'Royal Enfield', 200, 251999.00, '2-stroke')
print("The model is" , bike.model)
bike.brake()