# for i in range(1,6):
#     print(i)
# else:
#     print("End of loop")

a = 1
while a < 6:
    print (a)
    a = a + 1
    if a == 4:
        continue
    print ("After Continue")
else:
    print("End of while loop")
