#6.b To demonstrate polymorphism (method overloading without using #conditions) in Python using variable length arguments.
class Polymorph:
    def add(self, *numbers):
        return sum(numbers)

p = Polymorph()
print(p.add())
print(p.add(1))
print(p.add(1, 2))
print(p.add(1, 2, 3, 4))
print(p.add(2, 4, 6, 9, 6, 54))