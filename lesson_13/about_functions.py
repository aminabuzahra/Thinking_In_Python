# about functions:
# ================

# 1- Every function is an object
# 2- We can nest functions
# Example:

def a(x,y):
    
    def b(x):
        return x+5
    return b(x)+y

print (a(1,2))

# 3- functions can be passes as arguments
# 4- functions can be stored in variables

# 5- Since functions are objects, you can add properties to this function (object)

class Subhi:
    pass

s = Subhi()

s.name = "Subhi"
s.age = 30
s.add = lambda x,y : x+y

print (s.name)
print (s.age)

print (s.add(2,2))

def multiply(x,y):
    return x*y

multiply.z = 10

print (multiply.z)

print (multiply (3,7))

    
