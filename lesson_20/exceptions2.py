import random

class TrumpException(Exception):
    pass

class DatabaseNotFound(Exception):
    pass

def retreive_id_from_database(name):
    
    r = random.randint(1000, 9999)
    print(r)
    
    if 2000 < r < 3000:
    # if r >= 2000 and r <= 3000:
        raise DatabaseNotFound("Database not available!!")
    
    if name == "Trump":
        raise TrumpException("Trump not found!!")
    
    return str(r)

def close_connection():
    print ("Connection Closed!")

try:
    print (retreive_id_from_database("Abass"))
    
except TrumpException as e:
    print(e)
    
except DatabaseNotFound as e:
    print(e)
else:
    print("No Excpetions found :)")
finally:
    close_connection()
