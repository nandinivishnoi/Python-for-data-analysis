class Account:
    def __init__(self,bal,acc):
        self.balance=bal
        self.account=acc
        
    def debit(self,amount):
        self.balance-=amount
        print("Rs.", amount , " was debited from  your account")
        print("Total balance in your account is : ",self.get_balance())
   
    def creadit(self,amount):
        self.balance+=amount
        print("Rs." ,amount, " was creadited in your account")
        print("Total balance in yout account is : ",self.get_balance())
   
    def get_balance(self):
        return self.balance
    
acc1=Account(100000,827889)
acc1.debit(30000)
acc1.get_balance()

acc1.creadit(2000)
acc1.get_balance()
