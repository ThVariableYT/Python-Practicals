from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
# Implementing the interface in the rectangle class
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width=width
        self.height=height
    def area(self):
        return self.width*self.height
    def perimeter(self):
        return 2 * (self.width + self.height)
# Implementing the interface in a circle class
class Circle(Shape):
    def __init__(self, radius):
        self.radius=radius
    def area(self):
        return 3.14159 * self.radius * self.radius
    def perimeter(self):
        return 2 * 3.14159 * self.radius
# Creating instance of rectangle and circle
rectangle=Rectangle(3,4)
circle=Circle(4)
print(f"Rectangle area:{rectangle.area()}")
print(f"Rectangle perimeter:{rectangle.perimeter()}")
print(f"Circle area:{circle.area()}")
print(f"Circle perimeter:{circle.perimeter()}")
