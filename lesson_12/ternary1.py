def even_number(x):
    return "even" if x % 2 == 0 else "odd"

even_number_lambda = lambda x : "even" if x % 2 == 0 else "odd"
print (even_number_lambda(7))

# print (even_number(4))
# print (even_number(3))

x = 4
result = "even" if x % 2 == 0 else "odd"
# print(result)

# Syntax:
# value1 if condition else value2