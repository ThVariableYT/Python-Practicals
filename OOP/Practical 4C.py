class Student:

    def _init_(self):
        self.student_name = input("Enter student name: ")
        self.course = input("Enter course name: ")
        self.roll_no = int(input("Enter roll no.: "))
        self.div = input("Enter division: ")
        self.clg = input("Enter college name: ")

        print("\nPlease enter subject marks")
        self.Maths = int(input("Enter Maths marks: "))
        self.Oops = int(input("Enter OOPs marks: "))
        self.DBMS = int(input("Enter DBMS marks: "))
        self.WP = int(input("Enter WP marks: "))
        self.BC = int(input("Enter BC marks: "))
        self.ADP = int(input("Enter ADP marks: "))

    def display(self):
        print("\n------- STUDENT DETAILS -------")
        print("Name:", self.student_name)
        print("Course:", self.course)
        print("Roll No:", self.roll_no)
        print("Division:", self.div)
        print("College:", self.clg)

        print("\n------- MARKS -------")
        print("Maths:", self.Maths)
        print("OOPs:", self.Oops)
        print("DBMS:", self.DBMS)
        print("WP:", self.WP)
        print("BC:", self.BC)
        print("ADP:", self.ADP)


# Creating object and calling display
s1 = Student()
s1.display()