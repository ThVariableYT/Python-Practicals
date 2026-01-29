class add:
    def __init__(self,a):
            self.a=a
            #adding two objects
    def __add__(self,o):
            return self.a + o.a
obj1=add(1)
obj2=add(2)
obj3=add("fy")
obj4=add("it")
print(obj1+obj2)
print(obj3+obj4)