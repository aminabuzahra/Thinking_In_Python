def is_positive(x):
    return "positive" if x > 0 else "negative" if x < 0 else "none"

def is_positive2(x):
    if x > 0:
        return "positive"
    elif x < 0:
        return "negative"
    else:
        return "none"
    
x = 0
print (is_positive(x))