from typing import Protocol

class InterfaceExample(Protocol):
    
    def drive(self):
        ...

class ChilfOfInterface(InterfaceExample):
    pass

a = ChilfOfInterface()
a.drive()

def add_numbers(a,b):
    return a+b

a.new_method = add_numbers # binding methods

print(a.new_method(1,2))

# a.drive()