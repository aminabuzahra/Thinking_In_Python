class Engine:
    
    def __init__(self):
        self._rpm = 0
        
    def start(self):
        print ("Engine started")
        
    def stop(self):
        print ("Engine stoped")
    
    @property
    def rpm():
        return self._rpm
    
    @rpm.setter
    def rpm(speed):
        self._rpm = speed

class Wheel:
    
    def __init__(self):
        self._radial_velcoity = 0
        
    def rotate(self, radial_velcoity):
        self._radial_velcoity = radial_velcoity

class Body:
    
    def __init__(self, body_color):
        self.body_color = body_color

class Car: # Car has an Engine ==> Composition
    
    def __init__(self, engine, number_of_wheels): # engine is injected to this class
        
        self.body = Body("red") # strong composition
        
        self._engine = engine # Aggregation
        
        self.wheels = [] # strong composition
        for i in range(number_of_wheels):
            self.wheels.append(Wheel())
            
    def start(self): # delegation 
        self._engine.start()

class FlyingCar(Car): # FlyingCar is a Car ==> Inheritance
    pass

class SwimmingCar(Car): # SwimmingCar is a Car ==> Inheritance
    pass
        
class Brain:
    pass

class Human: #strong composition
    def __init__(self):
        self.brain = Brain()

engine_for_car = Engine()
engine_for_toktok = Engine()

fiat = Car(engine_for_car, 4)
toktok = Car(engine_for_toktok, 3)

print(len(fiat.wheels))

fiat.start()




        
    
    
    
        
    