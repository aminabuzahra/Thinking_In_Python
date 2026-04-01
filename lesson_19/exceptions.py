# handling exceptions:
# ===================
# syntax 1: catching exceptions
#   try:
#       # code that can raise exception
#   except [type of exception] [as object_name]:
        # code to handle the excpetion
#   except [type of exception] [as object_name]:
        # code to handle the excpetion
#   except [type of exception] [as object_name]:
        # code to handle the excpetion
#   else:
#       # code to run if there is not excpetion at all in the try block
#   default:
#       # code that run in all cases (with and without exceptions)
#  
#   syntax 2: raising exceptions
#   raise exception_type
#
#   syntax 3: creating new types of exception
#   my_exception(Exeption):
#       pass

def divide_by(a,b):
    return a / b

number = 1000
for i in range (20):
    print(divide_by(number, i - 10))

print("Subhi")

