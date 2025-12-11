class Book:

    def _init_(self):
        self.book_name = input("Enter book name: ")
        self.author_name = input("Enter author name: ")
        self.book_price = int(input("Enter price of book: "))
        self.total_copies = int(input("Enter total number of books: "))

    def generate_bill(self):
        print(" Purchase Details ".center(45, "-"))
        total_price = self.book_price * self.total_copies
        print("Book Name:", self.book_name)
        print("Author Name:", self.author_name)
        print("Price of book:", self.book_price)
        print("Total Copies:", self.total_copies)
        print("Total Price:", total_price)


# Object Creation
c = Book()
c.generate_bill()