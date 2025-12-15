class Bank:
  name=""
  acctno=0
  initial_bal=5000
  amt=0.0
  def __init__(self):
    print("enter name,acctno")
    self.name=input()
    self.acctno=int(input())
  def display(self):
      print("Customer Details")
      print(self.name)
      print(self.acctno)
      print(Bank.initial_bal)
  def deposit(self):
     print("enter amount to be deposited")
     self.amt=int(input())
     Bank.initial_bal=Bank.initial_bal+self.amt
     print("updated balance is",Bank.initial_bal)
  def withdraw(self):
     print("enter amount to be withdraw")
     self.amt=int(input())
     Bank.initial_bal=Bank.initial_bal-self.amt
     print("updated balance is",Bank.initial_bal)
b1=Bank()
b1.display()
b1.withdraw()
b1.deposit()
  

     
                  
    
