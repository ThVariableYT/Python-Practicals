class employee:
    def add(self, salary, incentive):
        self.a=(salary+incentive)
        print("Total salary in the base class",self.a+incentive)
        
class dept(employee):
    temp=("I am a member of department class")
    
    def add(self, salary, incentive):
        self.a=(salary+incentive)
        print(self.temp)
        print("Total salary in derive class:",self.a)
        e=dept()
        e.add(5555,7775)