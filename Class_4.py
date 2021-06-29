class Student:
    def __init__(self, firstname, lastname, age, bunk_classes, code_day):
        self.fn = firstname
        self.ln = lastname
        self.age = age
        self.bc = bunk_classes
        self.cd = code_day

    def student_details(self):
        return f'The student name is {self.fn}, {self.ln} .\n Age is {self.age} .' \
               f'\n And has bunked  {self.bc} classes till now .\n also does {self.cd}  codes per day'


s1 = Student("Lucifer", "Morningstar", 22, 13, 5)
print(s1.student_details())  # "return"  is used so "print" has to be written to call the the function
print(s1.cd)

s2= Student("Chloe","Deckor",20,5,8)
print(s2.student_details())
print(s2.cd)