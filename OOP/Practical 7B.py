class employee:
    def add(self, salary, incentive):
        self.a=(salary+incentive)
        increment=int(input("Enter the incrememnt income"))
        print("Total salary in the base class",self.a+incentive)
        
class dept(employee):
    temp=("I am a member of the department class.")
    
    def add(self, salary, incentive):
        self.a=(salary+incentive)
        print(self.temp)
        print("Total salary in derived class:",self.a)
        super(dept,self).add(salary,incentive)
        
e=dept()
e.add(5575, 9505)