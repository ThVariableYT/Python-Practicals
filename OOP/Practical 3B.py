class bank:
        def info(self,cust_name, acc_no,bal):
                self.cust_name=cust_name
                self.acc_no=acc_no
                self.bal=bal
        def deposit(self):
            dep_amt=int(input("Enter the amount to be deposit:")) 
            self.bal=self.bal+dep_amt
            print ("Current balance is:", self.bal)
        def withdraw(self):
            with_amt=int(input("Enter the amount to withdraw:")) 
            self.bal=self.bal-with_amt
            print("Current balance is:", self.bal)
c=bank()
cust_name=str(input("Enter your name"))
acc_no=int(input("Enter your account name"))
bal=int(input("Enter your balance"))
c.info(cust_name,acc_no,bal)
a=int(input("Enter 1 if you want to deposit and 2 if you want to withdraw:"))
if(a==1):
    c.deposit()
elif(a==2):
    c.withdraw()