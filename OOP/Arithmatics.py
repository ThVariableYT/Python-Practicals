class Arithmatic:
 
    def accept_data(self,a,b):
        self.a=a
        self.b=b
    def operation(self):
        add=self.a+self.b
        print("Addition is:", add)
        sub=self.a-self.b
        print("Defference is:", sub)
        multi=self.a*self.b
        print("Multiplication is:", multi)
        div=self.a/self.b
        print("Division is:", div)
al=Arithmatic()
print("Enter first no:")
a=int(input())
print("Enter second no:")
b=int(input())
al.accept_data(a,b)
al.operation()
