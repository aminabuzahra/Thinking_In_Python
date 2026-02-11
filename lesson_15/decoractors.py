# decorators (simplest way)
# =========================

def shout():
    print("YA SUBHI")

def add_number_decorator(function): # with a parameter that holds the wrapped function
    def wrapper():                  # Should be included and should be named exazcly wrapper()
        print ("before shouting")
        function()
        print ("after shouting")
        print ("==============")
    return wrapper                  # Should be written exactly like this 

shout = add_number_decorator(shout) # part of the syntax

shout()

# decorators 2
# ============
# @ syntax

def my_decortator(function): 
    def wrapper():                  
        print ("before function")
        function()
        print ("after function")
        print ("==============")
    return wrapper

@my_decortator
def laugh():
    print ("Ha Ha Ha Ha !")

@my_decortator
def speak():
    print ("Bla Bla Bla")   

laugh()
speak()

# decorators with parameters

def log(func):
    def wrapper(*args, **kwargs):   # Notics the parameters !
        print (f"This {func} function was called")
        func(*args, **kwargs)       # Notics the parameters !
    return wrapper                  # Notics there are no parameters !
    

def log_math(func):
    def wrapper(*args, **kwargs):     # Notics the parameters !
        print (f"This {func} function was called")
        return func(*args, **kwargs)  # Notics the parameters !
    return wrapper                    # Notics there are no parameters !

@log_math
def subtract(n2,n1):
    return n2 - n1

@log
def change_name_in_DB(old_name, new_name):
    pass

change_name_in_DB("Subhi", "Abbas")

print(subtract(5,3))

# Decorators that alter inputs and outpus
# 1. Altering input

def fixing_divide(func):
    def wrapper(*args, **kwargs):
        if args[1] == 0:
            return func(args[0], 1)
        else:
            return func(*args, **kwargs)
    return wrapper
        
@fixing_divide
def divide_numbers(number1, number2):
    return number1 / number2

print(divide_numbers(6,0))

#2. Altering output
def negative(func):
    def wrapper(*args, **kwargs):
        return -func(*args, **kwargs)
    return wrapper


# adding multiple decoraters to the same function

@negative
@log_math
def multiply_numbers(number1, number2):
    return number1 * number2

print (multiply_numbers(5,5))

# preventing calling the function
def check_password(func):
    def wrapper(password, *args, **kwargs):
        if (password == "100200300"):
            func(*args, **kwargs)
        else:
            print("Access Denied !")
    return wrapper
           

@check_password
def add_money_to_account(amount):
    print(f"Added {amount} to your account")

add_money_to_account("10200300", 10000000000)





    
        
    
    