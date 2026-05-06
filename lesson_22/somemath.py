class absolute_value_class():
    def absolute_value(self, num):
        return num if num >= 0 else -1 * num

def main():
    print(__name__)  # __main__
    absv = absolute_value_class()
    print(absv.absolute_value(5))
    print(absv.absolute_value(-5))
    print(absv.absolute_value(0))

if __name__ == "__main__":
   main()

"""
print(__name__) # __main__
if __name__ == "__main__":
    print("I ran from myself")
else:
    print("I was imported")
"""


