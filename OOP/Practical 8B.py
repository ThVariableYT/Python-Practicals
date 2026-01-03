#8b
class Add:
    def __init__(self, a):
        self.a = a   # initialize data member

    def __add__(self, other):
        return self.a + other.a   # overload + operator


# Creating objects with integer values
obj1 = Add(1)
obj2 = Add(2)

# Creating objects with string values
obj3 = Add("fy")
obj4 = Add("it")

# Performing addition using overloaded + operator
print(obj1 + obj2)   # Output: 3
print(obj3 + obj4)   # Output: fyit