#8d
class Num:
    def __init__(self, num):
        self.num = num

    def __gt__(self, other):
        return self.num > other.num


obj1 = Num(1)   # num = 1
obj2 = Num(4)   # num = 4

if obj1 > obj2:
    print("obj1 is greater than obj2")
else:
    print("obj2 is greater than obj1")