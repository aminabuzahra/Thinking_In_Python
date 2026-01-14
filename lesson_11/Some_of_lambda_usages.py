# Some of lambda usages
# 1- Sorting
# =======

a = [5,-2,4,2,10]
a.sort()

print(a)

d = [("Subhi", 3),
     ("Abbas", 1_000_000),
     ("Khader", 5),
     ("Jumaah", 4)
     ]

# def k(x):
#     return x[1]
#     
# d.sort(key = k)

d.sort(key = lambda x : x[1], reverse = True)

print(d)


# 1- sorting
# ============

# sorted() function syntax:
# sorted(list, key = lambda function)
# lambda function should return the values which should be sorted

d2 = {"Subhi" : 3,
      "Abbas" : 1_000_000,
      "Khader" : 5,
      "Jumaah" : 4
     }

sss = sorted(d2.items(), key = lambda x : x[1])
print (list(sss))


class Student:
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark
    
    def __str__(self):
        return f"Name is {self.name}, and mark = {self.mark}"

students = [Student("Subhi",55), Student("Khader", 70), Student("Abbas", 0)]
sss = list(sorted(students, key = lambda x: x.mark, reverse = True))

for i in sss:
    print(i)

# 2- filtering
# ============

# filter() function syntax:
# filter(lambda function, list)
# lambda function should return boolean; either True or False.
# if lambda function returns True, this element should be added
# if lambda function returns False, this element should be ignored

b = [1,2,3,4,5,6,7,8,9,10]
evens = list(filter(lambda x : x % 2 == 0, b))
print(evens)

# 3- mapping
# ==========

# map() function syntax:
# map(lambda function, list)
# lambda function should return value

x = list(map(lambda x : x * x, b))
print(x)
