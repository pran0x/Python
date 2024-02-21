class account:
   def __init__(self,balance, account_no):
      self.balance = balance
      self.account = account_no
      
   def details(self):
      print("Your account no is:",self.account)
      print("Your balance is:",self.balance)
      
   def debit(self, amount):
      self.balance -= amount
      print("Balance is:",amount,"Was Debited")
      print("Total balance is =", self.balance) 
      
   def credit(self,amount):
      self.balance += amount
      print("Balance is:",amount,"Was Credited")
      print("Your Balance is:",self.balance)
           
   def get_balance(self):
      print("Total Balance is:",self.balance)
      
p1 = account(10000,253535)
p1.details()
p1.debit(4000)
p1.credit(300)