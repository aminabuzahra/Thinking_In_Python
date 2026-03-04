class Person:

    def __init__(self, name): # Instance method ==> Needs self
        self._name = name

    @property
    def name(self):  # Instance method ==> Needs self
        return self._name

    @name.setter
    def name(self, name):  # Instance method ==> Needs self
        self._name = name

    def print_name(self):  # Instance method ==> Needs self
        print(self._name)

    def laugh(self, number_of_laughs):
        print("Ha" * number_of_laughs)

s = Person("Subhi")

s.name = "Abbas"
s.laugh(3)

print ("Ok")

def add_number(a,b): # module method. Does not need self
    return a+b


