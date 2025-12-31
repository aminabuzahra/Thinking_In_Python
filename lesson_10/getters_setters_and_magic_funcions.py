# getters, setters

class character:
    def __init__(self, name="somebody", age=33, b=10): # Constructor
        self.name = name
        self.age = age
        self._bonus = b
    
    @property # getter
    def bonus(self):
        return self._bonus + 5
    
    @bonus.setter # setter
    def bonus(self, bonus):
        if bonus > 100:
            self._bonus = 100
        else:
            self._bonus = bonus
            
#     def prnt(self):
#         print (f"Name: {self.name}, Age: {self.age}, Bonus = {self._bonus}")
        
    def __str__(self): # to string
        return (f"Name: {self.name}, Age: {self.age}, Bonus = {self._bonus}")
    
    def __gt__(self, obj): # greater than
        return self.age > obj.age

    def __lt__(self, obj): # less than
        return self.age < obj.age
    
    def __eq__(self, obj):
        return self.age == obj.age
    
#     def set_bonus(self, bonus):
#         if bonus > 100:
#             self._bonus = 100
#         else:
#             self._bonus = bonus
        
# subhi = character(input(),int(input()))
subhi = character()
print(subhi.name)
print(subhi.age)

print (subhi.bonus) # getting bonus value

# subhi.set_bonus(1000000)
subhi.bonus = 1000_000

print(subhi.bonus)

# subhi.prnt()
print(subhi)
subhi.name = "Subhi"
print(subhi)

abbas = character ("Abbas", 40, 90)
jumaah = character ("Abbas", 40, 90)
print (abbas)

if abbas > subhi:
    print("Abbas is older")
    
if subhi < abbas:
    print ("Subhi is younger")
    
if jumaah == abbas:
    print ("The same age")


