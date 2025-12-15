class Bank:
  name=""
  acctno=0
  initial_bal=0.0
  amt=0.0
  def accept(self):
    print("enter name,acctno")
    name=input()
    acctno=int(input())
    
    print("Customer Details")
    print(name)
    print(acctno)
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
b1.accept()
b1.withdraw()
b1.deposit()
  

     
                  
    
