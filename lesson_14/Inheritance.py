# Inheritance
class Animal: # Super class / Parent Class / Base Class
    
    def __init__(self):
        pass
    
    def make_sound(self):
        print("Animal Sound")
    
    def move(self):
        print("Move")

class Cat(Animal): # Subclass / Child class / type of Animal (Super class) 
    def make_sound(self):
        print("Meow")
    def move(self):
        print("Run")

class SmallFish(Animal):
    def make_sound(self):
        print("No sound")
        
    def move(self):
        print("Swim")

class Bird(Animal):
    def make_sound(self):
        print("Yozaqzek")
        
    def move(self):
        print("Fly")

class AnotherAnimal(Animal):
    ...

class AnotherAnotherAnimal(Animal):
    pass

# lucy = Animal()
# lucy = Cat()
# lucy.make_sound()
# lucy.move()

def sound(animal: Animal):
    animal.make_sound()
    
def move(animal: Animal):
    animal.move()
    

# Polymorphism
sound(Animal())
sound(Cat())
sound(SmallFish())
sound(Bird())

print ("="*10)

move(Animal())
move(Cat())
move(SmallFish())
move(Bird())

