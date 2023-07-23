class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        
    def __repr__(self):
        return f'<Car {self.make} {self.model}>'
    
class Garage:
    def __init__(self):
        self.cars = []
    def len(self):
        return len(self.cars)    
    def add_car(self, car):
        if not isinstance(car, Car):
            raise TypeError( f"it's not a type of Car. it's : {car.__class__}")
        self.cars.append(car)            

        
ford = Garage()
car = Car('Ford', 'Fiesta')
ford.add_car(car)

print(ford.len())
