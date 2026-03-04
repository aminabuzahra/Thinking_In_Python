class Test:

    @classmethod
    def print_something(cls):
        print("Something")

t = Test()
t.print_something() # A class method can be called from an instance
Test.print_something() # A class method can be called from the class directly


