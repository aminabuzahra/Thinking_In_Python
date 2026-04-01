# list ==> new other list
# syntax:
# new_item(expression) for item in list if condition
# list comprehensions can be used: list, string, tupple, dictionary

# Third Solution - List Comprehension
# =================================

def print_iterator(msg, lst):
    print(msg, end=" ")
    for item in lst:
        print(item, end=" ")
    print()


numbers = [1, 2, 3, 4, 5]
double_numbers = [item * 2 for item in numbers]  # like map()

print_iterator("doublenumbers:", double_numbers)

even_numbers = [item for item in numbers if item % 2 == 0]
print_iterator("even_numbers:", even_numbers)

booleans = [True, False, True, False, False]
filtered_trues = [item for item in booleans]

print_iterator("filtered_trues:", filtered_trues)

even_odd_strings = ["even" if item % 2 == 0 else "odd" for item in numbers]
print_iterator("even_odd_strings:", even_odd_strings)

even_odd_strings = [
    str(item) + ": even, " if item % 2 == 0 else str(item) + ": odd, "
    for item in numbers
]
print_iterator("even_odd_strings:", even_odd_strings)

even_odd_strings = [
    f"{item}: {"even" if item % 2 == 0 else "odd"}, " for item in numbers
]
print_iterator("even_odd_strings:", even_odd_strings)


# lis
new_name_of_trump = "Battikha"
new_name = [item for item in new_name_of_trump]

print(new_name)

my_tupple = (1, 2, 3, 4, 5)
add_one_to_my_tupple = tuple(item + 1 for item in my_tupple)
print(add_one_to_my_tupple)
print_iterator("my tupple =", add_one_to_my_tupple)
