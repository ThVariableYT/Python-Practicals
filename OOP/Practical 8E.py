#8e
class num:
    def __init__(self, num0):
        self.num0 = num0
        
    def __lt__(self, num1):
        if(self.num0<num1.num0):
            return "ob1 is less than ob2"
        else:
            return "ob2 is less than ob1"

    def __eq__(self, num2):
        if(self.num0==num2.num0):
            return "Both are equal"
        else:
            return "Not equal"
ob1 = num(4)
ob2 = num(5)
print(ob1 < ob2)
ob3 = num(5)
ob4 = num(5)
print(ob3 == ob4)