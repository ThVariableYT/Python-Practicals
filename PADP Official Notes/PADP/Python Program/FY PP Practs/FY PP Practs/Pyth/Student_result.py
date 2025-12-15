class Result:
  
  def accept(self):
    print("enter name,rollno,class and Batch")
    self.name=input()
    self.rollno=int(input())
    self.class_nm=input()
    self.batch=input()
  def adp_mks(self):
    print("enter theory,internal and practical marks of ADP out of 75,25 & 50")
    self.adp_ext=int(input())
    self.adp_int=int(input())
    self.adp_pr=int(input())
    self.adp_tot=self.adp_ext+self.adp_int+self.adp_pr
    print("ADP total")
    print(self.adp_tot)
  def oop_mks(self):
    print("enter theory,internal and practical marks of OOP out of 75,25 & 50")
    self.oop_ext=int(input())
    self.oop_int=int(input())
    self.oop_pr=int(input())
    self.oop_tot=self.oop_ext+self.oop_int+self.oop_pr
    print("OOP total")
    print(self.oop_tot)
  def display(self):
    print("Student Result")
    print(self.name)
    print(self.rollno)
    print(self.class_nm)
    print(self.batch)
    print(self.adp_ext)
    print(self.adp_int)
    print(self.adp_pr)
    print(self.adp_tot)
    print(self.oop_ext)
    print(self.oop_int)
    print(self.oop_pr)
    print(self.oop_tot)

  def final_result(self):
    self.result1=self.adp_tot+self.oop_tot
    self.per=100*self.result1/300
    print(self.per)
    
r1=Result()
r1.accept()
r1.adp_mks()
r1.oop_mks()
r1.display()
r1.final_result()
  

     
                  
    
