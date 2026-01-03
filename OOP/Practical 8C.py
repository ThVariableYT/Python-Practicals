#8c
class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def __add__(self, other):
        return Complex(self.real + other.real,
                       self.img + other.img)

    def __str__(self):
        return f"{self.real} + {self.img}i"


# Creating objects
o1 = Complex(1, 2)   # real = 1, img = 2
o2 = Complex(3, 4)   # real = 3, img = 4

# Adding two complex numbers
o3 = o1 + o2

# Printing result
print(o3)