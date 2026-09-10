# Student Management System

A simple **Student Management System** built using Python and Object-Oriented Programming (OOP).
This project allows users to add, view, search, update, and delete student records through a menu-driven console application.

## Features

* Add a new student
* View all student records
* Search for a student using Student ID
* Update student information
* Delete a student record
* Exit the application

## Student Details

Each student record contains:

* Student ID
* Name
* Age
* Course
* Branch
* Marks

## Technologies Used

* **Python 3**
* **Object-Oriented Programming (OOP)**
* Python List
* Classes and Objects
* `while` loop
* `for` loop
* Conditional statements
* User input

## Project Structure

```text
Student-Management-System/
│
├── student_management.py
└── README.md
```

## How to Run

### 1. Install Python

Make sure Python 3 is installed on your computer.

Check the Python version:

```bash
python --version
```

### 2. Clone the Repository

```bash
git clone <your-github-repository-url>
```

### 3. Open the Project Folder

```bash
cd Student-Management-System
```

### 4. Run the Program

```bash
python student_management.py
```

## Menu

When the program starts, the following menu is displayed:

```text
===== STUDENT MANAGEMENT SYSTEM =====

1. Add student
2. View students
3. Search student
4. Update student
5. Delete student
6. Exit
```

## How It Works

### Add Student

Select option `1` and enter:

```text
Student ID
Name
Age
Course
Branch
Marks
```

The student information is stored as an object inside a list.

### View Students

Select option `2` to display all stored student records.

### Search Student

Select option `3` and enter the Student ID.

The program searches the list and displays the student's details if found.

### Update Student

Select option `4`, enter the Student ID, and choose which information you want to update.

You can update:

* Name
* Age
* Course
* Branch
* Marks

### Delete Student

Select option `5` and enter the Student ID to remove the student's record.

### Exit

Select option `6` to close the application.

## OOP Concepts Used

This project uses basic Object-Oriented Programming concepts.

### Class

```python
class Student:
```

The `Student` class represents a student.

### Constructor

```python
def __init__(self, student_id, name, age, course, branch, marks):
```

The constructor initializes the student information.

### Object

```python
student = Student(student_id, name, age, course, branch, marks)
```

A student object is created using the `Student` class.

### List

```python
students = []
```

The list stores multiple student objects.

## Example

```text
Enter your choice: 1

Enter the student id: 101
Enter the student name: Alok
Enter the student age: 22
Enter the course: BE
Enter the branch: AIML
Enter the student marks: 85

=== STUDENT ADDED SUCCESSFULLY ===
```

## Future Improvements

The project can be improved by adding:

* File/database storage
* Login system
* Input validation
* Duplicate Student ID checking
* GUI interface
* Sorting students by marks
* Percentage and grade calculation
* MySQL database integration
* Flask/Django web application

## Learning Outcomes

Through this project, you can learn:

* Python fundamentals
* Classes and objects
* Lists
* Loops
* Conditional statements
* CRUD operations
* User input handling
* Basic project structure

## Author

**Alok Khandare**

BE – Artificial Intelligence and Machine Learning
Ghousia College of Engineering, Ramanagara

## License

This project is created for **educational and learning purposes**.
