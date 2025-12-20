#7. b To implement polymorphism using method overriding in Python and to access the base class method using super().
class Employee:
    def add(self, salary, incentive):
        total=salary+incentive
        increment = int(input("Enter the increament amount:"))
        print("Total salary in base class:",total+increment)
class Dept(Employee):
    message= "I am a member of department class"

    def add(self, salary, incentive):
        total=salary+incentive 
        print(self.message)
        print("Total salary in derived class:", total)
        super().add(salary, incentive)
d = Dept()
d.add(5575, 9505)