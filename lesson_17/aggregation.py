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

class AccountingSystem: # Agreegation (Weak Composition)
    
    def __init__(self, database = TestDatabase()): # database injection
        self._database = database
        
    def store_accounting_interaction(self, data): # delegation
        self._database.store_record(data)
    
    @property
    def database(self):
        return self._database
    
    @database.setter
    def database(self, database_engine):
        self._database = database_engine

mongoDB = MongoDB()
redis = Redis()
mySQL = MySQL()
test = TestDatabase()

accounting = AccountingSystem(mongoDB)
accounting.store_accounting_interaction("Got 1 million dollar")

accounting.database = redis
accounting.store_accounting_interaction("Got Another 1 million dollar")

accounting.database = mySQL
accounting.store_accounting_interaction("Got Another 1 million dollar")

accounting.database = test
accounting.store_accounting_interaction("Got Another 1 million dollar")
