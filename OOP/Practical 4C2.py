class Student:
    def _init_(self):
        self.student_name = input("Enter student name: ")
        self.course = input("Enter course name: ")
        self.roll_no = int(input("Enter roll no.: "))
        self.div = input("Enter division: ")
        self.clg = input("Enter college name: ")

        print("\nPlease enter subject marks")
        self.Maths = int(input("Enter Maths marks: "))
        self.Oops = int(input("Enter OOPS marks: "))
        self.DBMS = int(input("Enter DBMS marks: "))
        self.WP = int(input("Enter WP marks: "))
        self.BC = int(input("Enter BC marks: "))
        self.ADP = int(input("Enter ADP marks: "))

        print("\n================ RESULT ================\n")

    def generate_result(self):
        total_marks = self.Maths + self.Oops + self.DBMS + self.WP + self.BC + self.ADP
        avg_marks = total_marks / 6
        percentage = (total_marks / 600) * 100

        print("Student Name:", self.student_name)
        print("Course Name:", self.course)
        print("Roll No.:", self.roll_no)
        print("Division:", self.div)
        print("College Name:", self.clg)

        print("\n---- Marks ----")
        print("Maths:", self.Maths)
        print("OOPS:", self.Oops)
        print("DBMS:", self.DBMS)
        print("WP:", self.WP)
        print("BC:", self.BC)
        print("ADP:", self.ADP)

        print("\nTotal Marks:", total_marks)
        print("Average Marks:", avg_marks)
        print("Percentage:", percentage)

    def _del_(self):
        print("Object deleted")


# Create object and call methods
c = Student()
c.generate_result()

del c