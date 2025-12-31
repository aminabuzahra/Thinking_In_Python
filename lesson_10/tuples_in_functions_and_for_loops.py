def sum_and_multiply(x,y):
    return x+y, x*y

# s, m = sum_and_multiply(5,5)
# 
# print (f"s = {s}, m = {m}")

# ==========================


a = [(1,2), (2,3), (4,5)]

for x, y in a:
    s, m = sum_and_multiply(x,y)
    print (f"s = {s}, m = {m}")
