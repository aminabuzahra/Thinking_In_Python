# Another Exmample of Polymorphism
class Animal: 
    
    def __init__(self):
        pass
    
    def make_sound(self):
        print("Animal Sound")
    
    def move(self):
        print("Move")

class Cat(Animal): 
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
        

list_of_animals = [Animal(), Cat(), Bird(), SmallFish()]

for animal in list_of_animals: # Pure Polymorphism
    animal.make_sound()
    
b = Bird()

# to check type you use either isinstance(object, Class / Base Class) or type(object) is Class / Base Class
print (isinstance(b, Animal))
print (isinstance(b, Bird))
print (isinstance(b, Cat))

print (type(b) is Bird)
print (type(b) is Animal)