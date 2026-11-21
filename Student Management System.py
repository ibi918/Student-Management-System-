import json
import os

FILE_NAME = "students.json"


# Load student records from file
def load_students():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


# Save student records to file
def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)


# Calculate percentage and grade
def calculate_grade(marks):
    total = sum(marks)
    percentage = total / len(marks)

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

    return percentage, grade


# Add a new student
def add_student(students):
    roll_no = input("Enter Roll Number: ")

    for student in students:
        if student["roll_no"] == roll_no:
            print("Student already exists!")
            return

    name = input("Enter Student Name: ")

    marks = []

    for i in range(1, 6):
        while True:
            try:
                mark = float(input(f"Enter marks for Subject {i} (0-100): "))

                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("Marks must be between 0 and 100.")

            except ValueError:
                print("Please enter a valid number.")

    student = {
        "roll_no": roll_no,
        "name": name,
        "marks": marks
    }

    students.append(student)
    save_students(students)

    print("Student added successfully!")


# View all students
def view_students(students):
    if not students:
        print("No student records found.")
        return

    for student in students:
        percentage, grade = calculate_grade(student["marks"])

        print("\n---------------------------")
        print("Roll Number:", student["roll_no"])
        print("Name:", student["name"])
        print("Marks:", student["marks"])
        print("Percentage:", round(percentage, 2), "%")
        print("Grade:", grade)


# Search for a student
def search_student(students):
    roll_no = input("Enter Roll Number to Search: ")

    for student in students:
        if student["roll_no"] == roll_no:
            percentage, grade = calculate_grade(student["marks"])

            print("\nStudent Found!")
            print("Name:", student["name"])
            print("Roll Number:", student["roll_no"])
            print("Marks:", student["marks"])
            print("Percentage:", round(percentage, 2), "%")
            print("Grade:", grade)
            return

    print("Student not found!")


# Update student information
def update_student(students):
    roll_no = input("Enter Roll Number to Update: ")

    for student in students:
        if student["roll_no"] == roll_no:
            student["name"] = input("Enter New Name: ")

            marks = []

            for i in range(1, 6):
                while True:
                    try:
                        mark = float(input(f"Enter new marks for Subject {i} (0-100): "))

                        if 0 <= mark <= 100:
                            marks.append(mark)
                            break
                        else:
                            print("Marks must be between 0 and 100.")

                    except ValueError:
                        print("Please enter a valid number.")

            student["marks"] = marks

            save_students(students)

            print("Student updated successfully!")
            return

    print("Student not found!")


# Delete a student
def delete_student(students):
    roll_no = input("Enter Roll Number to Delete: ")

    for student in students:
        if student["roll_no"] == roll_no:
            students.remove(student)
            save_students(students)

            print("Student deleted successfully!")
            return

    print("Student not found!")


# Main program
def main():
    students = load_students()

    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_student(students)

        elif choice == "2":
            view_students(students)

        elif choice == "3":
            search_student(students)

        elif choice == "4":
            update_student(students)

        elif choice == "5":
            delete_student(students)

        elif choice == "6":
            print("Thank you for using Student Management System!")
            break

        else:
            print("Invalid choice! Please select 1-6.")


if __name__ == "__main__":
    main()