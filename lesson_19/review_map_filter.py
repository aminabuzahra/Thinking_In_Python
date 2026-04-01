# list ==> new other list

# First solution
# ==============
numbers = [1, 2, 3, 4, 5]
double_numbers = []


def print_list(msg, lst):
    print(msg, end=" ")
    for item in lst:
        print(item, end=" ")
    print()


for i in range(len(numbers)):
    double_numbers.append(numbers[i] * 2)

print_list("double numbers:", double_numbers)

# Second Solution (map(), filter())
# =================================

# numbers ==> even_numbers

# def check_even(n):
#     return n % 2 == 0
# even_numbers = list(filter(check_even, numbers))

even_numbers = list(filter(lambda n: n % 2 == 0, numbers))

print_list("even numbers:", even_numbers)

double_numbers2 = list(map(lambda n: n * 2, numbers))

print_list("double numbers 2:", double_numbers2)

booleanss = [True, False, True, True]
opposite_booleans = list(map(lambda x: not x, booleanss))

print_list("opposite_booleans", opposite_booleans)

filtered_booleans = list(filter(lambda x: not x, booleanss))
print_list("filtered_booleans", filtered_booleans)
