# d = { "Name" : "Subhi",
#       "Salary" : 1_000_000
#     }
# 
# print (d["Name"])
# print (d["Salary"])

# def add(x,y):
#     return x+y
# 
# def subtract(x,y):
#     return x-y
# 
# op = {"+" : add,
#       "-" : subtract
#      }

op2 = {"+" : lambda x,y : x + y,
       "-" : lambda x,y : x - y,
       "*" : lambda x,y : x * y,
       "/" : lambda x,y : x / y
      }

while True:
    x = int(input())
    y = int(input())
    oper = input()
    print (op2[oper](x,y))
