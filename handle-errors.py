class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __repr__(self):
        return f'<Car {self.make} {self.model}>'
    
class Garage:
    def __init__(self) -> None:
        self.cars = []
    
    def __len__(self):
        return len(self.cars)
    def add_car(self, car):
        if not isinstance(car, Car):
            #valueError
            raise TypeError(f'Tried to add a {car.__class__} to the garage, but you can only add type Car')
        self.cars.append(car)


ford = Garage()
fiesta = Car('Ford', 'Fiesta')
try:
    ford.add_car('fiesta')
# Only catch TypeError
except TypeError:
    print('your car was no a Car!')
except ValueError:
    print('A weird error happened')
finally:
    print(f' the Garage now has {len(ford)}')