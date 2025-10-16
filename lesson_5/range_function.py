# numbers = [1,2,3,4,5,6,7,8,9,10]

for number in range(1, 1000_000): # range is a lazy function
    if number < 10:
        print(number)

for number in range(2,11):
    if number % 2 == 0:
        print(number)

for number in range(2, 11, 2): # steps
    print(number)
    
for number in range(10, 0, -1): # reverse
    print(number)
    