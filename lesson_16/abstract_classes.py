from abc import ABC, abstractmethod

class MyMath(ABC):
    
    def __init__(self, name):
        self._name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value
    
    def count_to_ten(self):
        for i in range(1,11):
            print(i)
    
    @abstractmethod
    def add_numbers(self, a,b): # method signature
        ... # must be implemented
    

class ImplementedMyMath(MyMath):
    def add_numbers(self, a : int,b : int):
        return a+b
    
class ImplementedMyMathString(MyMath):
    def add_numbers(self, a : str, b : str):
        return f"{a}_{b}"
        
mym = ImplementedMyMath("subhi")
mym_string = ImplementedMyMathString("subhi")

arr = [ImplementedMyMath("subhi"), ImplementedMyMathString("abass")]

mym.name = "Khalili"
mym.count_to_ten()
print(mym.name)

for i in arr:
    print(i.name)
    print(i.add_numbers(3,5))

# print(mym.add_numbers(3,5))
# print(mym_string.add_numbers(3,5))





