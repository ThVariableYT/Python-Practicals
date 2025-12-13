#5.C Multilevel inheritance
class Company:
    def _getdata(self):
        self.ename=str(input("Enter company name:")) 
        self.location=str(input("Enter location:"))
class employee(Company):
    def _getempdata(self):
        self.id=int(input("Enter employee id:")) 
        self.ename=str(input("Enter Employee name:")) 
        self.designation=str(input("Enter Designation:")) 
        self.Bsalary=float (input("Enter basic salary:")) 
class payroll(employee):
    def calculate_sal(self):
        self.TA=0.15*self.Bsalary
        self.DA=0.70*self.Bsalary
        self.HRA=0.25*self.Bsalary
        self.PF=0.1*self.Bsalary
        self.PT=0.2*self.Bsalary
        netsalary=self.Bsalary+self.TA+self.DA+self.HRA-self.PF-self.PT
        print("Net_salary is: ",netsalary)
c=payroll()
c._getdata()
c._getempdata()
c.calculate_sal()