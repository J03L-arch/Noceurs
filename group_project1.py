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
s2= Student("Unc", "13245", "079876543", "Business")
s3= Student("Kim", "14235", "0723456789", "Engineering")

students.append(s1)
students.append(s2)
students.append(s3)

for student in students:
    student.display()

while True:
    print("\n---School Management System---")
    print("1.Add Student")
    print("2.View Students")
    print("3.Exit")

    choice= input("Enter your choice: ")
    
    if choice== "1":
        name= input("Enter student name: ")
        id_number= input("Enter student ID number: ")
        course= input("Enter course: ")

        student= Student(name, id_number, course)
        students.append(student)

        print("Student added successfully!")
        
    elif choice=="2":
        if len(students)==0:
            print("No students found")
        else:
            for student in students:
                student.display()

    elif choice== "3":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Try again")









