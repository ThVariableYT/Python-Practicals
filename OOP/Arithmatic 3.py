class Arithmatic:

    def accept_data(self, a,b):
        self.a=a
        self.b=b
    def addition(self, a,b):
        add=self.a+self.b
        print("Addition is:", add)
    def subtraction(self, a,b):
        sub=self.a-self.b
        print("Defference is:", sub)
    def multiplication(self, a,b):
        multi=self.a*self.b
        print("Multiplication is:", multi)
    def division(self, a,b):
        div=self.a/self.b
        print("Division is:", div)

al=Arithmatic()
print("Enter first no:")
a=int(input())
print("Enter second no:")
b=int(input())
al.accept_data(a,b)
c=str(input("Type 'add' if you want to Add the two numbers, 'sub' if you want to Subtract the two numbers, 'multi' if you want to Multiply the two numbers and 'div' if you want Divide the two numbers:"))
if(c=="add"):
    al.addition(a,b)
elif(c=="sub"):
    al.subtraction(a,b)
elif(c=="multi"):
    al.multiplication(a,b)
elif(c=="div"):
    a1.division(a,b)
