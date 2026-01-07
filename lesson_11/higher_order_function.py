# Calculator using higher order function calculate()
while True:
    
    print ("Enter the first number:", end = " ")
    a = int(input())
    
    print ("Enter the second number:", end = " ")
    b = int(input())
    
    print ("Enter the operator (q for quit):", end = " ")
    operation = input()

    def add(x,y):
        return x+y

    def subtract(x,y):
        return x-y

    def multiply(x,y):
        return x*y

    def divide(x,y):
        return x/y

    def modulo(x,y):
        return x%y

    def floor_division(x,y):
        return x//y
    
    def calculate(x,y,func): # Higher Order Function
        return func(x,y)

    print ("=====================")
    print ("The result is =", end = " ")
    
    if operation == "+":
        print(calculate(a,b,add))
        
    elif operation == "-":
        print(calculate(a,b,subtract))
        
    elif operation == "*":
        print(calculate(a,b,multiply))
        
    elif operation == "/":
        print(calculate(a,b,divide))
 
    elif operation == "%":
        print(calculate(a,b,modulo))
 
    elif operation == "//":
        print(calculate(a,b,floor_division))
 
    elif operation == "q":
        break;
    
    print("=====================")
    print()



