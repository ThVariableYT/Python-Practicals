#5.b Multiple inheritance 
class base1(object): 
    def __init__(self): 
        self.str1="hello" 
        print(self.str1) 
        print("base1") 
class base2(object): 
    def __init__(self): 
        self.str2="hii" 
        print(self.str2) 
        print("base2")
class derived(base1, base2): 
    def __init__(self):
        base1.__init__(self)
        base2.__init__(self)
        print("derived")
    def displayStr(self):
        print(self.str1, self.str2)
c=derived()
c.displayStr()