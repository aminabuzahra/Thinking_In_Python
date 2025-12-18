# Dictionaries

a = {
    "name" : "Subhi",
    "age" : 50,
    "bank balance" : 5
    }

books = {
    "JavaScript" : 75,
    "Thinking in Python" : 100,
    "Thinking in C++ I" : 200,
    "Thinking in C++ II" : 150
}

# print (a["name"])
# print (a["age"])
# print (a["bank balance"])

a["age"] = 60

# print (a["age"])

a["hobbies"] = "Gossiping"

# print (a["hobbies"])

del a["hobbies"]

# print (a)

# for i in books:
#     print (i)
    
for i in books.keys():
    print(i)
    
for i in books.values():
    print (i)

for i, j in books.items():
    print (i, j)
    
for i in books:
    print(i, books[i])
