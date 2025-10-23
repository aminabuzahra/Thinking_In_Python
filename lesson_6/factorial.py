# recusrion

# factorials
# 5! = 5*4*3*2*1
# 3! = 3*2*1
# 7! = 7*6*5*4*3*2*1

def factorial(n):
    
    if n < 0:         
        return None
    elif n == 1:                # IMPORTANT: Stopping condition
        return 1 
    
    return n * factorial(n - 1) # recursion

a = factorial(5)

print(a)
