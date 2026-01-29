class complex:
    def __init__(self, real, img):
        self.real=real
        self.img=img
    def __add__(self, other):
        return self.real+other.real, self.img+other.img
    def __str__(self):
        return self.real, self.img
o1=complex(1,2)
o2=complex(3,4)
o3=o1+o2
print(o3)