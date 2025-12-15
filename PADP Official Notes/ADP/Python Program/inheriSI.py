class Shape:
    def _get_length_breadth(self):
        self._length=int(input("enter rectangle length :"))
        self._breadth=int(input("enter rectangle bredth:"))

class Rectangle(Shape):
    def calculate(self):
        print("Area of rectangle: ",self._length*self._breadth)

        
rect=Rectangle()
rect._get_length_breadth()
rect.calculate()
