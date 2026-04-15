def divide(x, y):
    try:
        result = x / y
    except:
        print("Please do not divide by zero")
        return 0
    
    return result

while True:
    x = float(input("Enter x: "))
    if x == 0:
        break
    y = float(input("Enter y: "))
    print(f"Result = {divide (x, y)}")
    print("=" * 10)
    print()

print("Abbas")
