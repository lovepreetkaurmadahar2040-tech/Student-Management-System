'''Problem Statement

Create a Student Management system using python and Object Oriented Programming(OOP)

The System should allow the user to:-

Add a new student.
View all Students.
Search for a student using student ID
Update a student's marks
Delete a student record using student ID
Display the student with the highest marks
Exit the application
Student Details

Each Student should have:-
 
Student ID
Student Name
Age
Marks '''

class Student:
    def __init__(self,id,name,age,marks):
        self.id=id
        self.name=name
        self.age=age
        self.marks=marks
    def details(self):
        print(F"Student ID:- {self.id}") 
        print(F"Student Name:- {self.name}") 
        print(F"Student Age:- {self.age}") 
        print(F"Student Marks:- {self.marks}") 
s1=Student(1234,"Jiya",12,90) 
s2=Student(4567,"tia",16,89)  
s1.details()

class Student_management:
    def __init__(self):
        self.list=[]
    def add_stu(self):
        id=int(input("Enter the ID:- "))
        name=input("Enter the Name:- ")
        age=int(input("Enter the age:- "))
        marks=float(input("Enter the marks:- "))

        student=Student(id,name,age,marks)
        self.list.append(student)
        print("Student details added successfully")

    def view_details(self):
        if len(self.list)==0:
            print("Student not found") 
        else:
           for student in self.list:
              print(student.details())

    def search_student(self):
        id=int(input("Enter the id:- "))
        for  student in self.list:
            if id ==student.id: 
                student.details()
                return 
            else:
                print("Student ID not fount")  
                
    def re_move(self): 
        id=int(input("Enter the id:- "))
        for  student in self.list:
            if id ==student.id: 
                self.list.remove(student) 
                print("Student detail deleted")
            else:
                print("Student ID not fount")                          


s= Student_management()
s.view_details()
print(s.list)
s.add_stu()
s.view_details()
s.search_student()
s.re_move()
     
class Student:
    def __init__(self, student_id, name, age, marks):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.marks = marks

    def display(self):
        print("\nStudent ID :", self.student_id)
        print("Name       :", self.name)
        print("Age        :", self.age)
        print("Marks      :", self.marks)


class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def add_students(self):
        student_id = int(input("Enter Student ID : "))
        name = input("Enter Student Name : ")
        age = int(input("Enter Age : "))
        marks = float(input("Enter Marks : "))

        student = Student(student_id, name, age, marks)
        self.students.append(student)

        print("Student Added Successfully!")

    def view_students(self):
        if len(self.students) == 0:
            print("No Students Found!")
        else:
            for student in self.students:
                student.display()

    def search_student(self):
        student_id = int(input("Enter Student ID to Search : "))

        for student in self.students:
            if student.student_id == student_id:
                print("Student Found!")
                student.display()
                return

        print("Student Not Found!")

    def update_marks(self):
        student_id = int(input("Enter Student ID : "))

        for student in self.students:
            if student.student_id == student_id:
                new_marks = float(input("Enter New Marks : "))
                student.marks = new_marks
                print("Marks Updated Successfully!")
                return

        print("Student Not Found!")

    def delete_student(self):
        student_id = int(input("Enter Student ID : "))

        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                print("Student Deleted Successfully!")
                return

        print("Student Not Found!")

    def display_topper(self):
        if len(self.students) == 0:
            print("No Students Available!")
        else:
            topper = self.students[0]

            for student in self.students:
                if student.marks > topper.marks:
                    topper = student

            print("\nTopper Details")
            topper.display()

sms = StudentManagementSystem()

while True:

    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Display Topper")
    print("7. Exit")

    choice = int(input("Enter Your Choice : "))

    if choice == 1:
        sms.add_students()

    elif choice == 2:
        sms.view_students()

    elif choice == 3:
        sms.search_student()

    elif choice == 4:
        sms.update_marks()

    elif choice == 5:
        sms.delete_student()

    elif choice == 6:
        sms.display_topper()

    elif choice == 7:
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")