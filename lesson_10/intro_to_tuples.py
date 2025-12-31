# tuples

a = [10,20,30] # list (array)
a[0] = 30
print (a)

a2 = tuple(a)
print (a2)

t = (1,2,3) # tuple is immutable, i.e cannot be changed!! Carved in stone
print (len(t))

t2 = list(t)
t2.append(4)
t2[0] = 50
print (t2)


d = { "Subhi" : 5}
