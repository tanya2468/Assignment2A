from managers.student_manager import StudentManager
from models.student import Student, GraduateStudent
from utils.validation import (
    is_valid_id, is_valid_name, is_valid_department, is_valid_thesis, is_valid_marks, is_valid_choice
)


def main():
    manager = StudentManager()

    while True:
        print("\nWelcome to Student Performance Tracker")
        print("1. Add Student \n2. Remove Student \n3. Add Scores \n4. List All Students \n5. Top Scorer in Subject \n6. Department Average \n7. Exit")
        choice = input("Enter the choice: ").strip()
        if not is_valid_choice(choice, [1, 2, 3, 4, 5, 6, 7]):
            print("Invalid choice. Please enter a number between 1 and 7.")
            continue

        if choice == "1":
            student_type = input("Type (student/graduate): ").strip().lower()
            id = input("ID: ").strip()
            name = input("Name: ").strip()
            dept = input("Department: ").strip()

            if not is_valid_id(id) or not is_valid_name(name) or not is_valid_department(dept):
                print("Invalid entries. Please try again.")
                continue

            if student_type == "graduate":
                thesis = input("Thesis Title: ").strip()
                if not is_valid_thesis(thesis):
                    print("Invalid thesis entry.")
                    continue
                student = GraduateStudent(id, name, dept, thesis)
            else:
                student = Student(id, name, dept)

            if manager.get_student_by_id(id) is not None:
                print(f"Student with ID {id} already exists.")
            else:
                manager.add_student(student)

        elif choice == "2":
            id = input("Enter the ID of the Student to be removed: ").strip()
            if not is_valid_id(id):
                print("Invalid ID entry.")
                continue
            manager.remove_student(id)

        elif choice == "3":
            id = input(
                "Enter the ID of the student whose marks you want to enter: ").strip()
            if not is_valid_id(id):
                print("Invalid ID entry.")
                continue

            student = manager.get_student_by_id(id)
            if student is None:
                print(f"No student found with ID: {id}")
                continue

            print("Enter subjects and marks (type 'X' to finish):")
            while True:
                subject = input("Subject: ").strip()
                if subject.upper() == 'X':
                    break
                marks = input(f"Marks for {subject}: ").strip()
                if not is_valid_marks(marks):
                    print("Invalid marks. Try again.")
                    continue
                student.add_score(subject, float(marks))
                print(f"Added {marks} for {subject}.")
            print("Scores added.")

        elif choice == "4":
            students = manager.list_students()
            if not students:
                print("No students found.")
            for student in students:
                print(student)

        elif choice == "5":
            sub = input(
                "Enter the subject for checking the top scorer: ").strip()
            top_student = manager.get_top_scorer(sub)
            if top_student:
                print(
                    f"Top scorer in {sub}: {top_student.name} with {top_student.scores[sub]} marks.")
            else:
                print(f"No scores found for subject: {sub}")

        elif choice == "6":
            dept = input(
                "Enter the department for the average calculation: ").strip()
            avg = manager.get_department_average(dept)
            print(f"Average score for department {dept}: {avg:.2f}")

        elif choice == "7":
            print("Thank you for using Student Performance Tracker!")
            exit()


if __name__ == "__main__":
    main()
