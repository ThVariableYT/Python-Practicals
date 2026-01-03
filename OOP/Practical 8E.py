#8e
class Num:
    def __init__(self, num):
        self.num = num

    def __lt__(self, other):
        return self.num < other.num

    def __eq__(self, other):
        return self.num == other.num


ob1 = Num(4)
ob2 = Num(5)
print("ob1 < ob2 :", ob1 < ob2)

ob3 = Num(5)
ob4 = Num(5)
print("ob3 == ob4 :", ob3 == ob4)