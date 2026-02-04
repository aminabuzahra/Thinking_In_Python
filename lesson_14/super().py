class Vehicle:
    def __init__(self, name):
        self._name = name
    
    def move(self):
        print(f"{self._name} moving")
    
    def brake(self):
        print(f"{self._name} braking")

class Car():
    def __init__(self, name, car_type):
        super().__init__(name)
        self._car_type = car_type
    
    def move(self):
        print(f"{self._name} car moving")

bmw = Car("BMW", "Jeep")
bmw.move()
bmw.brake()