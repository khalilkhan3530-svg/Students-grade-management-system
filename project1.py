students_grade = { }

def add_student(name, grade):
    students_grade[name] = grade
    print(f"{name} with {grade} added successfully")

def update_student(name,grade):
    if name in students_grade:
        students_grade[name] = grade
        print(f"{name } with {grade} updated successfully")
    else:
        print(f"{name} not found")

def delete_student(name):
    if name in students_grade:
        del students_grade[name] 
        print(f"{name} deleted successfully")
    else:
        print(f"{name} not found")

def display_all_students():
    if students_grade:
        for name,grade in students_grade.items():
            print(f"{name} : {grade}") 
    else:
        print("No students available")        

display_all_students()

def main():
    while True:
        print("\n STUDENTS GRADES MANAGEMENT SYSTEM")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. View Students")
        print("5. Exit")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            name = input("Enter your name: ")
            grade = int(input("Enter your grade: "))
            add_student(name, grade)

        elif choice == 2:
            name = input("Enter student name: ")
            grade = int(input("Enter Student grade: "))    
            update_student(name, grade)

        elif choice == 3:
            name = input("Enter Student name: ")    
            delete_student(name)

        elif choice == 4:
            display_all_students()

        elif choice == 5 :
            print("Closing the Program")       
            break

        else:
            print("Invalid choice")


main()