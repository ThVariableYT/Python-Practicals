#5.a Single inheritance
#Befine base class Shape
class Shape:
    #Function to initialize the data members def get Length Breadth(self):
    def _get_Length_Breadth(self):
        self.length=int(input("Enter length:"))
        self.breadth=int(input("Enter breadth:"))
#Defining derived class Rectangle'
class Rectangle(Shape):
    #Fuunction to calculate area of rectangle  
    def calculate_area(self):
        print("area of Rectangle is", self.length* self.breadth)
#Creating object
obj=Rectangle
#Calling function to get input
obj._get_Length_Breadth()
#Calling function to get the area of rectangle
obj.calculate_area()