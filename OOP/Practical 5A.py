#5.a Single inheritance
#Define base class Shape
class Shape:
    #Function to initialize the data members def get Length Breadth(self):
    def _get_Length_Breadth(self):
        self._length=int(input("Enter length:"))
        self._breadth=int(input("Enter breadth:"))
#Defining derived class Rectangle'
class Rectangle(Shape):
    #Function to calculate area of rectangle  
    def calculate_area(self):
        print("area of Rectangle is", self._length* self._breadth)
#Creating object
obj=Rectangle()
#Calling function to get input
obj._get_Length_Breadth()
#Calling function to get the area of rectangle
obj.calculate_area()