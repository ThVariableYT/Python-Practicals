class Examination:

    def _init_(self):
        self.sname = input("Enter the name of student: ")
        self.rollno = int(input("Enter the roll no of student: "))
        self.course = input("Enter the course: ")
        self.div = input("Enter the division: ")
        self.sem = input("Enter the semester: ")

        # Initialize subject marks (default 0)
        self.oops = 0
        self.dbms = 0
        self.wp = 0
        self.bc = 0

    # Subjects with 100 marks
    def subject_100(self):
        if self.oops < 50:
            self.oops = int(input("Enter the marks of OOPS (out of 100): "))
        else:
            print("Error: OOPS marks must be below 50 initially.")

        if self.dbms < 50:
            self.dbms = int(input("Enter the marks of DBMS (out of 100): "))
        else:
            print("Error: DBMS marks must be below 50 initially.")

    # Subjects with 50 marks
    def subject_50(self):
        if self.wp < 25:
            self.wp = int(input("Enter the marks of WP (out of 50): "))
        else:
            print("Error: WP marks must be below 25 initially.")

        if self.bc < 25:
            self.bc = int(input("Enter the marks of BC (out of 50): "))
        else:
            print("Error: BC marks must be below 25 initially.")

    # Display function
    def display(self):
        print("\n----- STUDENT DETAILS -----")
        print("Student Name:", self.sname)
        print("Roll No:", self.rollno)
        print("Course:", self.course)
        print("Division:", self.div)
        print("Semester:", self.sem)

        print("\n----- MARKS -----")
        print("OOPS (100):", self.oops)
        print("DBMS (100):", self.dbms)
        print("WP (50):", self.wp)
        print("BC (50):", self.bc)


# Create object and use methods
obj = Examination()
obj.subject_100()
obj.subject_50()
obj.display()