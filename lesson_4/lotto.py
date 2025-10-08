import random

number = int(input("Enter a number between 1-10: "))

correct_number = random.randint(1, 10)

if number == correct_number:
    print (f"You won {1000000:,} Shekels")
else:
    print (f"Looser")
    
print (f"Correct answer is: {correct_number}")
