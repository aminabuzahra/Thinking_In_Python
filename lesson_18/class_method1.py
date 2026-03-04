class Person:

    def __init__(self, name):
        self._name = name

    def print_who_i_am(self):
        print(self._name)

    @classmethod
    def create_person(cls, name, age, salary = 0, *data): # data is of tuple type (like array/list but without altering the elements
        person = cls(name)
        person._age = age
        person._salary = salary
        person._data = data
        return person

class Champion(Person):
    def __init__(self, name):
        super().__init__(name)
        # self._name = name

    def print_who_i_am(self):
        print(f"I am champion {self._name} in programming")

    # ctr + / for comment out code

    # def __init__(self, name, age): # this constructor (the last constructor is adopted)
    #     self._name = name
    #     self._age = age

khamis = Person("Ali")
affash = Person.create_person("Affash", 14)

fadi = Champion.create_person("Fadi", 22)
fadi.print_who_i_am()

print (f"{affash._name} is {affash._age} years old")






