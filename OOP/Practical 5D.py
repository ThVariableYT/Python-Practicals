# 5.D hirarchical inheritance
class shape:
    def __init__(self, color):
        self.color = color
    def area(self):
        pass
class circle(shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2
class square(shape):
    def __init__(self, color, length):
        super().__init__(color)
        self.length = length
    def area(self):
        return self.length ** 2
circle=circle("red",3)
square=square("yellow",5)
print(circle.area())
print(square.area())