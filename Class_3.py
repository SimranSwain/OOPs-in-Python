class Student:
    def __init__(self, firstname, lastname, age, bunk_classes, code_day):
        self.fn = firstname
        self.ln = lastname
        self.age = age
        self.bc = bunk_classes
        self.cd = code_day

    def student_details(self):
        # return f'The student name is {self.fn}, {self.ln} .\n Age is {self.age} .\n He
        # has bunked \n {self.bc} classes till now .\n He does {self.cd}  codes per day'
        print(self.fn, self.ln, "is age of ",self.age," \n And  has ", self.bc, " bunked classes.\n also does ", self.cd,
              " codes per day ")       # see the  below two points

        # here "print"  is used so "print" has to be written to call the the function
        # BUT  "None"  is coming in output as function isn't returning anything


s1 = Student("Lucifer", "Morningstar", 22, 13, 5)
print(s1.student_details())
s2= Student("Chloe","Deckor",20,5,8)
print(s2.student_details())
print(s1.cd)
print(s2.cd)
