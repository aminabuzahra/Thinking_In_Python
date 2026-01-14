# lambda functions:
# =================

# 1- functions without names
# 2- one line expression (using statements is forbidden)
#    expressions can be: arithmatic and logical expressions
# 3- always return a value (but do not use return statement

# Syntax:
# lambda parameters : expression
# paramateres can be 0, or 1, or many

add = lambda x,y : x+y

print (add(1,2))

power = lambda x : x * x
print (power(3))

p = lambda : print("Subhi")
p()

even = lambda x : "even" if x % 2 == 0 else "odd"
print (even(9))


