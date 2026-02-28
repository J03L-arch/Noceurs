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
        print("_______________________________________________")
import os

students= []
filename="students.txt"

if os.path.exists(filename):
    with open(filename, "r") as f:
        next(f)
        for line in f:
            name,phone_number,id_number,course= line.strip().split(",")
            students.append(Student(name, id_number, phone_number, course))

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
    print("3.Change Student Course")
    print("4.Export Students to File")
    print("5.Delete Student")
    print("6.Exit")
    

    choice= input("Enter your choice: ")
    
    if choice== "1":
        name= input("Enter student name: ")
        id_number= input("Enter student ID number: ")
        phone_number= input("Enter phone number: ")
        course= input("Enter course: ")

        student= Student(name, id_number, phone_number, course)
        students.append(student)

        print("Student added successfully!")
        
    elif choice=="2":
        if len(students)==0:
            print("No students found")
        else:
            for student in students:
                student.display()
    
    elif choice == "3":
        search_name= input("Enter the name of student to student to update: ")
        found= False
        for student in students:
            if student.name== search_name:
                new_course= input(f"Enter new course for {student.name}: ")
                student.change_course(new_course)
                print(f"{student.name}'s course has been updated to {new_course}!")
                found= True
                break
            if not found:
                print(f"No student found with the name {search_name}.")


    elif choice== "4":
        if len(students)== 0:
            print("No student to export")
        else:
            filename= input("Enter file name to save(eg., students.txt):")
            with open(filename, "w") as f:
                f.write("name, phone number, id number, course\n")

                for student in students:
                    f.write(f"{student.name}, {student.id_number}, {student.phone_number} {student.course}\n")

            print(f"All current students have been exported to {filename}")

    elif choice=="5":
        delete_name= input("Enter student name to delete: ")
        found= False

        for student in students:
            if student.name== delete_name:
                students.remove(student)
                print(f"{delete_name} has been removed from the system.")
                found= True
                break

        if not found:
            print("Student not found")

    elif choice== "6":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Try again")









