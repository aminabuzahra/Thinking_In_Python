name = input("Enter you name: ")
age = input("Enter your age:")
number = int(input("Enter a number:"))

print("Hello " + name + "! Your age is: " + age + " The (number + 2) is: " + str(number + 2))

# f strings:

print(f"Hello {name}! Your age is: {age} The (number + 2) is: {number + 2}")

# other way:
print("Hello" , name , "! Your age is:" , age , "The (number + 2) is:" , number + 2)

# + sign means addition here
print (number + number)

# Arithmatic Operations:
# ==============================

print(1+1) # 2
print(5-3) # 2
print(2*3) # 6
print(10 / 2) # 5

print(11/2) # 5.5
print(11 // 2) # 5
print(11 % 2) # 1

print(3 ** 5) # 3 * 3 * 3 * 3 * 3
print (25 ** 0.5) # 5

# Priorities in Arithmatic Operations:
# PEMDAS
# Parenthesis ( )  الأقواس
# Exponent القوة **
# Multiply, Division ضرب
# Addition Subtraction جمع
# Left يسار
# Right يمين

print( 3 * 3 + 3 / 3 - 3 ) #7

# Comparison operators, result True or False
# >
# <
# >=
# <=
# ==  يساوي
# !=  لا

age = 19
adult = age > 17 # True
print (adult)

wealth = 1_030_010_083
forbidden = wealth < 1_000_000

print(forbidden)

number = int(input("enter a guess: "))
correct = number <= 11
print(correct)

number = int(input("enter a guess: "))
correct = number >= 12 and number <= 15 # 12 -> 15
print(correct)

# Logical Operators
# and
# True and True => True
# True and False => False
# False and True => False
# False and False => False

# or
# True or True => True
# True or False => True
# False or True => True
# False or False => False

# not
# not True => False
# not False => True

number = int(input("enter a guess: "))
correct = number <= 12 or number >= 15
print(correct)

a = True
b = not a
print (b)

# assignment operators:

a = 10

a += 10 # a = a + 1
a -= 3
a *= 2
a /= 2
a %= 17

b = 2
b **= 2

print(a)
print(b)

# math functions
# round

tomato_bill = 10.532_876
bill = round(tomato_bill , 2)
print (bill)
