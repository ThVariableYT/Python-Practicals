class Examination:

    def _init_(self):
        self.sname = input("Enter the name of student: ")
        self.rollno = int(input("Enter the roll no of student: "))
        self.course = input("Enter the course: ")
        self.div = input("Enter the division: ")
        self.sem = input("Enter the semester: ")

        # initialize all subject marks
        self.oops = 0
        self.dbms = 0
        self.wp = 0
        self.ss = 0
        self.adp = 0
        self.bc = 0

    def subject_100(self):
        self.oops = int(input("Enter the marks of OOPS (out of 50): "))
        if self.oops > 50:
            print("Error: Marks cannot exceed 50")

        self.dbms = int(input("Enter the marks of DBMS (out of 50): "))
        if self.dbms > 50:
            print("Error: Marks cannot exceed 50")

    def subject_50(self):
        self.wp = int(input("Enter the marks of WP (out of 25): "))
        self.ss = int(input("Enter the marks of SS (out of 25): "))
        self.adp = int(input("Enter the marks of ADP (out of 25): "))
        self.bc = int(input("Enter the marks of BC (out of 25): "))

    def external(self):
        print("\n--- EXTERNAL MARKS ---")
        self.subject_100()
        self.total_ext50 = self.oops + self.dbms

        self.subject_50()
        self.total_ext25 = self.wp + self.ss + self.adp + self.bc

    def internal(self):
        print("\n--- INTERNAL MARKS ---")
        self.subject_100()
        self.total_int50 = self.oops + self.dbms

        self.subject_50()
        self.total_int25 = self.wp + self.ss + self.adp + self.bc

    def result(self):
        self.external()
        self.internal()

        self.total = self.total_ext50 + self.total_ext25 + self.total_int50 + self.total_int25

        print("\nTotal Result:", self.total)
        self.per = (self.total / 400) * 100
        print("Percentage:", round(self.per, 2), "%")


# MAIN OBJECT
a1 = Examination()
a1.result()