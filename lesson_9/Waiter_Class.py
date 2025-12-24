class Waiter:
    
    n = ""   # self.n / Property / State
    t = []   # self.t / Property / State
     
    def __init__(self, name, tables): # constructor
        self.n = name
        self.t = tables
    
    def receive_order(self):    # method
        print (f"{self.n} receives orders")

khamis = Waiter("Khamis", [1,2,3]) # Instatitae Waiter Class / Calls the constructor __init__()

# khamis.n = "Khamis"
# khamis.t = [1,2,3]

khamis.receive_order()
print (khamis.t)

jumaah = Waiter("Jumaah", [4,5,6]) # Calls the constructor __init__()
# jumaah.name = "Jumaah"
# jumaah.tables = [4,5,6]

jumaah.receive_order()
print (jumaah.t)