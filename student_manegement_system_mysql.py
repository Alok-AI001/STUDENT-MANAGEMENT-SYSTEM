class Student:
    def __init__(self, student_id, name, age, course, branch, marks):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.course = course
        self.branch = branch
        self.marks = marks


print("===== STUDENT MANAGEMENT SYSTEM =====")

choice = ""
students = []

while choice != "6":
    print("\n1. Add student")
    print("2. View students")
    print("3. Search student")
    print("4. Update student")
    print("5. Delete student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        student_id = int(input("Enter the student id: "))
        name = input("Enter the student name: ")
        age = int(input("Enter the student age: "))
        course = input("Enter the course: ")
        branch = input("Enter the branch: ")
        marks = int(input("Enter the student marks: "))
        
        student = Student(student_id, name, age, course, branch, marks)
        students.append(student)
        print("=== STUDENT ADDED SUCCESSFULLY ===")

    elif choice == "2":
        print("==== STUDENT DETAILS ===")
        if not students:
            print("No student records found.")
        else:
            print("------------------------------")
            for student in students:
                print("student_id :", student.student_id)
                print("name       :", student.name)
                print("age        :", student.age)
                print("course     :", student.course)
                print("branch     :", student.branch)
                print("marks      :", student.marks)
                print("------------------------------")

    elif choice == "3":
        print("=== SEARCH STUDENT ===")
        student_id = int(input("Enter the student id to search: "))
        found = False
        for student in students:
            if student.student_id == student_id:
                print("Student found:")
                print("student_id :", student.student_id)
                print("name       :", student.name)
                print("age        :", student.age)
                print("course     :", student.course)
                print("branch     :", student.branch)
                print("marks      :", student.marks)
                found = True
                break
        if not found:
            print("Student not found.")

    elif choice == "4":
        print("=== UPDATE STUDENT ===")
        student_id = int(input("Enter the student ID to update: "))
        
        found_student = None
        for student in students:
            if student.student_id == student_id:
                found_student = student
                break

        if found_student is None:
            print("Student not found.")
        else:
            print("1. Update name")
            print("2. Update age")
            print("3. Update course")
            print("4. Update branch")
            print("5. Update marks")

            update_choice = input("Enter your choice: ")

            if update_choice == "1":
                found_student.name = input("Enter the new name: ")
                print("Name updated successfully.")
            elif update_choice == "2":
                found_student.age = int(input("Enter the new age: "))
                print("Age updated successfully.")
            elif update_choice == "3":
                found_student.course = input("Enter the new course: ")
                print("Course updated successfully.")
            elif update_choice == "4":
                found_student.branch = input("Enter the new branch: ")
                print("Branch updated successfully.")
            elif update_choice == "5":
                found_student.marks = int(input("Enter the new marks: "))
                print("Marks updated successfully.")
            else:
                print("Invalid choice.")

    elif choice == "5":
        print("=== DELETE STUDENT ===")
        student_id = int(input("Enter the student id to delete: "))
        deleted = False
        for student in students:
            if student.student_id == student_id:
                students.remove(student)
                print("Student deleted successfully.")
                deleted = True
                break
        if not deleted:
            print("Student not found.")

    elif choice == "6":
        print("Thank you for using the student management system!")
        break

    else:
        print("Invalid choice. Please try again.")