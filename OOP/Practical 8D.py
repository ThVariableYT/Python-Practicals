#8d
class num:
    def __init__(self, num):
        self.num = num

    def __gt__(self, num1):
        if(self.num>num1.num):
            return True
        else:
            return False
obj1 = num(1)
obj2 = num(4)
if (obj1 > obj2):
    print("obj1 is greater than obj2")
else:
    print("obj2 is greater than obj1")