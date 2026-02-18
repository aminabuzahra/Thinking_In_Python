class MyMath:
    
    def __init__(self, name):
        print (f"Constructed MyMath: {name}")
    
    def add_numbers(self, a,b):
        return a+b

class AdvancedMath(MyMath):
    def __init__(self, name):
        super().__init__(name)
        print (f"Constructed AdvancedMath: {name}")
    
    def subtract_number(self, a,b):
        return a - b
    
    def add_numbers(self, *a):
        sum = 0
        for i in a:
            sum += i 
        return sum
    
    def test_pass(self):
        # return ==> breaks the function / method
        for _ in range(3):
            print("Subhi")
            # pass ==> can be used anywhere
            # conitnue ==> can be used only in loops
            # break ==> can be used only in loops
            # ... ==> objecy of type ellipsis. Means you must implement this code
            # print(type(...))
            print("Abass")
            print("*"*5)

my_math = MyMath("my_math")
advanced_math = AdvancedMath("advanced_math")

print(my_math.add_numbers(3,4))
print(advanced_math.add_numbers(3,4,5,6))
advanced_math.test_pass()
