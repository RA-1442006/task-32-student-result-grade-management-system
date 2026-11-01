# main.py
# entry point for the Student Result & Grade Management System
# Task 32 - Veda Technology Internship

import os
from student_manager import (
    load_students_from_file,
    add_student,
    view_all_students,
    search_student,
    update_student,
    delete_student
)
from summary import display_performance_summary


def print_menu():
    print("\n" + "=" * 52)
    print("   STUDENT RESULT & GRADE MANAGEMENT SYSTEM")
    print("         (Veda Technology Internship)")
    print("=" * 52)
    print("1. Add Student Record")
    print("2. View All Students")
    print("3. Search Student (by Roll No or Name)")
    print("4. Update Student Details or Marks")
    print("5. Delete Student Record")
    print("6. View Class Performance Summary")
    print("7. Exit Program")
    print("=" * 52)


def main():
    # setup path for data storage
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_file = os.path.join(base_dir, "data", "students.json")

    # load existing records
    students = load_students_from_file(data_file)
    print(f"Loaded {len(students)} student record(s) from database.")

    while True:
        print_menu()
        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            add_student(students, data_file)

        elif choice == "2":
            view_all_students(students)

        elif choice == "3":
            search_student(students)

        elif choice == "4":
            update_student(students, data_file)

        elif choice == "5":
            delete_student(students, data_file)

        elif choice == "6":
            display_performance_summary(students)

        elif choice == "7":
            print("\nThank you for using the Student Result & Grade Management System!")
            print("All changes have been saved. Exiting...\n")
            break

        else:
            print("\nInvalid choice! Please enter a number between 1 and 7.")


if __name__ == "__main__":
    main()
