class Arithmatic:

    def accept_data(self):
        print("Enter first no:")
        self.a=int(input())
        print("Enten second no:")
        self.b=int(input())

    def operation(self):
        add=self.a+self.b
        print("Addition is:",add)
        sub=self.a-self.b
        print("Defference is:",sub)
        multi=self.a*self.b
        print("Multiplication is:",multi)
        div=self.a/self.b
        print("Division is:",div)
al=Arithmatic()
al.accept_data()
al.operation()
