# Remember! in python there is no overloading. Use * instead.
class MathSubhi:
    def add_numbers(self, *numbers):
        sum = 0
        for i in numbers:
            sum += i
        return sum       
    
m = MathSubhi()
print(m.add_numbers([1,2,5,7,9]))