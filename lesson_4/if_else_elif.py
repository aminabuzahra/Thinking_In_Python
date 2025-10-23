age = int(input("Enter your age: "))

# <= 2 ==> free
# <= 12 ==> 7 NIS
# < 18 ==> 15 NIS
# >= 18 ==> 30 NIS

if age <= 2:
    print("Free Payment")
elif age <= 12:
    print("7 NIS")
elif age < 18:
    print("15 NIS")
else:
    print("30 NIS")
