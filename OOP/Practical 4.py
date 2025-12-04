class Book:
    
        def __init__(self):
            self.book_name=str(input("Enter a book's name:"))
            self.author_name=str(input("Enter author's name:"))
            self.book_price=int(input("Enter the book's price:"))
            self.total_copies=int(input("Enter the total number of copies to purchase:"))
            
        def generate_bill(self):
            print("Purchase Details".center(45,"-"))
            book_price=self.book_price*self.total_copies
            print("Book Name:",self.book_name)
            print("Author's Name:",self.author_name)
            print("Total copies sold:",self.total_copies)
        def __del__(self):
            print("Destructor called and object deleted.")
        def check(self):
            print("I am present")
c=Book()
c.generate_bill()
##del (c)
c.check()
