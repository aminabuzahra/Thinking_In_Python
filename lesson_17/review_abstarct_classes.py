from abc import ABC, abstractmethod

class Car(ABC): # abstract class
    def __init__(self, name):
        self._name = name
    
    @abstractmethod
    def drive(self):
        ...
        
    @abstractmethod
    def park(self):
        ...
    
    @property
    def name(self):
        return self._name

class BenzineCar(Car):
    def __init__(self, name):
        self._name = name
    
    def drive(self):
        print (f"Car {self._name} is now driving")
        
    def park(self):
        print (f"Car {self._name} is now parking")
        
        
class ElectricCar(Car):
    def __init__(self, name):
        self._name = name
    
    def drive(self):
        print (f"Electric Car {self._name} is now driving")
    
    def park(self):
        print (f"Electric Car {self._name} is now parking")

class Parking():
    def park(self, car : Car):
        car.park()
    
t = Test()
fiat = BenzineCar("Fiat")
mercedes = BenzineCar("Mercedes")
electric_mercedws = ElectricCar("Mercedes 1500")

fiat.drive()
mercedes.drive()
electric_mercedws.drive()

subhi_parking = Parking()

subhi_parking.park(fiat)
subhi_parking.park(mercedes)
subhi_parking.park(electric_mercedws)

print (fiat.name)