# Inheritance
class Animal: # Super class / Parent Class / Base Class
    
    def __init__(self, name):
        self._name = name
    
    def make_sound(self):
        print(f"{self._name} Sound")
    
    def move_animal(self):
        print(f"{self._name} Move")

class Cat(Animal):
    def make_sound(self):
        print(f"{self._name} cat Sound")
    
    def move_animal(self):
        print(f"{self._name} cat Move")


lucy = Cat("Lucy")

lucy.make_sound()
lucy.move_animal()
        