# 4- min() / max()
# ================
# functions syntax:
# min(dictionary object d, d.get

d2 = {"Subhi" : 3,
      "Abbas" : 1_000_000,
      "Khader" : 5,
      "Jumaah" : -4
     }

#minimum

minimum = min(d2, key = d2.get)
print (minimum)

minimum = min(d2.items(), key = lambda x : x[1])
print (minimum)

minimum = min(d2.values())
print (minimum)

# maximum

maximum = max(d2, key = d2.get)
print (maximum)

maximum = max(d2.items(), key = lambda x : x[1])
print (maximum)

maximum = max(d2.values())
print (maximum)