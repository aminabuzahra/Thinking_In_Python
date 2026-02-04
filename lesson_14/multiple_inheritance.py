# multiple inhertiance

class Animal: 
    
    def __init__(self, name):
        self._name = name
    
    def make_sound(self):
        print("Animal Sound")
    
    def move(self):
        print("Move")

class Rideable:
    
    def __init__(self):
        pass
    
    def ride(self):
        print(f"Ride {self._name}")
        
class Horse(Animal, Rideable):
    pass

class Cat(Animal): 
    def make_sound(self):
        print("Meow")
    def move(self):
        print("Run")

lucy = Cat("Lucy")
lucy.make_sound()

alkaser = Horse("Alkaser")
alkaser.ride()

print (Horse.mro())
print (Horse.__mro__)

