class Bank_Account:
    
    def __init__(self, ib):
        self._balance = ib

    @property                     # Getter
    def balance(self):
        return self._balance
    
    @balance.setter               # Setter
    def balance(self, value):
        self._balance = value

    def get_balance(self):        # Getter
        return self._balance
    
    def set_balance(self, value): # Setter
        self._balance = value
    
    def add_balance(self, deposit):
        self._balance += deposit
        
    def subtract_from_balance(self, value):
        if (self._balance - value) < 0:
            print ("You are not allowed to be in minus")
        else:
            self._balance -= value
        
       
subhi_bank_account = Bank_Account(50)
print(subhi_bank_account._balance) # X
print(subhi_bank_account.get_balance()) # V
print(subhi_bank_account.balance) # V

subhi_bank_account.add_balance(10)
print(subhi_bank_account.balance)

subhi_bank_account.subtract_from_balance(15)
print(subhi_bank_account.balance)

subhi_bank_account.set_balance(1_000_000)
subhi_bank_account.subtract_from_balance(50)
print(subhi_bank_account.balance)
