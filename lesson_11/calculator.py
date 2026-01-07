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

    print ("=====================")
    print ("The result is =", end = " ")
    
    if operation == "+":
        print(add(a,b))
        
    elif operation == "-":
        print(subtract(a,b))
        
    elif operation == "*":
        print(multiply(a,b))
        
    elif operation == "/":
        print(divide(a,b))
 
    elif operation == "%":
        print(modulo(a,b))
 
    elif operation == "//":
        print(floor_division(a,b))
 
    elif operation == "q":
        break;
    
    print("=====================")
    print()