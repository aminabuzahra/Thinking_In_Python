from abc import ABC, abstractmethod

class Database:
    @abstractmethod
    def store_record(self, data):
        ...

class MongoDB(Database):
    def store_record(self, data):
        print (f"{data} Record is stored in MongoDB")

class MySQL(Database):
    def store_record(self, data):
        print (f"{data} Record is stored in MySQL")

class Redis(Database):
    def store_record(self, data):
        print (f"{data} Record is stored in Redis")

class TestDatabase(Database): # Fake database
    def store_record(self, data):
        print (f"Just testing")

class AccountingSystem: # Association (Weakest Composition)
    
    def __init__(self): # no injection !
        pass
        
    def store_accounting_interaction(self, data, database): # delegation
        database.store_record(data)

mongoDB = MongoDB()
redis = Redis()
mySQL = MySQL()
test = TestDatabase()

accounting = AccountingSystem()
accounting.store_accounting_interaction("Got 1 million dollar", mongoDB)
accounting.store_accounting_interaction("Got Another 1 million dollar", redis)
accounting.store_accounting_interaction("Got Another 1 million dollar", mySQL)
accounting.store_accounting_interaction("Got Another 1 million dollar", test)
