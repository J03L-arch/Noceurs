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

student_1= Student("Joe", 12345, 254676767, "Architecture")
student_2= Student("Steve", 67890, 254696969, "Agriculture")
student_3= Student("Kimberly", 54321, 254020202, "Computer Science")
student_4= Student("Trixi", 90876, 254777777, "Filming")
student_5= Student("Bena", 10293, 254333333, "Data Science")

#Display students
def display_info(self):
    print("Name:", self.name)
    print("ID:", self.id_number)
    print("Phone number:", self.phone_number)
    print("Course:", self.course)

display_info(student_1)

#Assign new courses
student_1.change_course("Civil Engineering")
student_2.change_course("Dehorning")
student_3.change_course("Data Science")
student_4.change_course("Music production")
student_5.change_course("Computer Science")

display_info(student_4)

