def is_even(x):
    return x % 2 == 0

def print_even(f, x):
    if f(x):
        print("even")
    else:
        print("odd")

print_even(is_even, 9)

##############################################
def print_even2(x):
    
    def is_even2(x):
        return x % 2 == 0
    
    if is_even2(x):
        print("even")
    else:
        print("odd")

print_even2(10)
