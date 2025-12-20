class Polymorph:
    def greet(self, name=None, rank=None):
        if name or rank:
            print("Hello", name, ", your rank is", rank)
        else:
            print("Hello student, your rank is 45")

p = Polymorph()
p.greet("Pallavi", 1)
p.greet("Anita")
p.greet()