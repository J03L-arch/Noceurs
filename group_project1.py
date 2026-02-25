#Name: Joel Mwega
#Date: 23/02/2026
#Program: To register students

#Register new students
class Student():
    def __init__ (self, name, id_number, phone_number, course):
        self.name= name
        self.id_number= id_number
        self.phone_number= phone_number
        self.course= course

    def change_course(self, new_course):
        self.course= new_course

#Display students
    def display(self):
        print("Name:", self.name)
        print("ID:", self.id_number)
        print("Phone number:", self.phone_number)
        print("Course:", self.course)

students= []
s1= Student("Joe", "12345", "0720374671", "Computer Science")
students.append(s1)

for student in students:
    student.display()





