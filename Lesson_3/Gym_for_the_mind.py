name = input("Enter your name: ")
age = int(input("Enter your age: "))

message_1 = "Your age is between 18 and 35"   # True
message_2 = "Go Habibi !"                     # True

checking_age = age >= 18 and age <=35

output_message = (checking_age and message_1) or message_2

print (output_message)
