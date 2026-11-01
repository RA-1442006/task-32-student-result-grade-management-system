# student_manager.py
# functions to add, view, search, update, and delete student records

import json
import os
from grade_calculator import (
    validate_roll_no,
    validate_mark,
    calculate_total,
    calculate_percentage,
    calculate_grade,
    calculate_status
)


def load_students_from_file(file_path):
    # read json file if it exists
    if not os.path.exists(file_path):
        return []

    try:
        with open(file_path, "r") as f:
            data = json.load(f)
            return data
    except Exception as e:
        print(f"Notice: Could not load data file ({e}). Starting with empty list.")
        return []


def save_students_to_file(student_list, file_path):
    # ensure directory exists before saving
    directory = os.path.dirname(file_path)
    if directory and not os.path.exists(directory):
        os.makedirs(directory, exist_ok=True)

    try:
        with open(file_path, "w") as f:
            json.dump(student_list, f, indent=2)
        return True
    except Exception as e:
        print(f"Error saving data: {e}")
        return False


def view_all_students(student_list):
    # check if list is empty
    if not student_list:
        print("\nNo student records found.")
        return

    print("\n" + "=" * 92)
    print(f"{'Roll No':<10} {'Name':<22} {'Department':<22} {'Total':<8} {'Percentage':<12} {'Grade':<8} {'Status':<8}")
    print("-" * 92)

    for student in student_list:
        roll = str(student.get("roll_no", ""))
        name = str(student.get("name", ""))
        dept = str(student.get("department", ""))
        total = f"{student.get('total', 0.0):.2f}"
        pct = f"{student.get('percentage', 0.0):.2f}%"
        grade = str(student.get("grade", ""))
        status = str(student.get("status", ""))

        print(f"{roll:<10} {name:<22} {dept:<22} {total:<8} {pct:<12} {grade:<8} {status:<8}")

    print("=" * 92)
    print(f"Total Students: {len(student_list)}\n")


def search_student(student_list):
    if not student_list:
        print("\nNo student records available to search.")
        return

    query = input("\nEnter Roll Number or Name to search: ").strip()
    if not query:
        print("Search query cannot be empty.")
        return

    # find matches (case insensitive partial match)
    matches = []
    for student in student_list:
        roll_match = query.lower() in str(student.get("roll_no", "")).lower()
        name_match = query.lower() in str(student.get("name", "")).lower()
        if roll_match or name_match:
            matches.append(student)

    if not matches:
        print(f"No student found matching '{query}'.")
        return

    print(f"\nFound {len(matches)} matching student(s):")
    print("-" * 60)
    for student in matches:
        print(f"Roll Number : {student['roll_no']}")
        print(f"Name        : {student['name']}")
        print(f"Department  : {student['department']}")
        print("Subject Marks:")
        for subj, mark in student.get("marks", {}).items():
            print(f"  * {subj:<18}: {mark:.2f}")
        print(f"Total Marks : {student.get('total', 0):.2f}")
        print(f"Percentage  : {student.get('percentage', 0):.2f}%")
        print(f"Grade       : {student.get('grade', '')}")
        print(f"Result      : {student.get('status', '')}")
        print("-" * 60)


def add_student(student_list, file_path):
    print("\n--- Add New Student ---")

    # get valid roll number
    while True:
        roll_input = input("Enter Roll Number: ").strip()
        is_valid, result = validate_roll_no(roll_input, student_list)
        if is_valid:
            roll_no = result
            break
        print(f"Error: {result} Please try again.")

    # get student name
    while True:
        name = input("Enter Student Name: ").strip()
        if name != "":
            break
        print("Error: Name cannot be empty.")

    # get department/class
    while True:
        dept = input("Enter Class / Department: ").strip()
        if dept != "":
            break
        print("Error: Department cannot be empty.")

    # get number of subjects
    while True:
        num_str = input("Enter number of subjects: ").strip()
        if num_str.isdigit() and int(num_str) > 0:
            num_subjects = int(num_str)
            break
        print("Error: Please enter a positive number for subjects.")

    # enter subjects and marks
    marks_dict = {}
    print("Now enter subject names and marks (0 - 100):")
    for i in range(num_subjects):
        while True:
            subj_name = input(f"  Enter Subject {i+1} Name: ").strip()
            if subj_name == "":
                print("  Error: Subject name cannot be empty.")
            elif subj_name in marks_dict:
                print("  Error: Subject already added. Enter a different subject.")
            else:
                break

        while True:
            mark_str = input(f"  Enter marks for {subj_name}: ").strip()
            valid_mark, mark_val = validate_mark(mark_str)
            if valid_mark:
                marks_dict[subj_name] = mark_val
                break
            print(f"  Error: {mark_val} Try again.")

    # calculate total, percentage, grade and pass/fail status
    total = calculate_total(marks_dict)
    percentage = calculate_percentage(marks_dict)
    grade = calculate_grade(percentage)
    status = calculate_status(percentage)

    new_student = {
        "roll_no": roll_no,
        "name": name,
        "department": dept,
        "marks": marks_dict,
        "total": total,
        "percentage": percentage,
        "grade": grade,
        "status": status
    }

    student_list.append(new_student)
    save_students_to_file(student_list, file_path)
    print(f"\nStudent '{name}' (Roll No: {roll_no}) added successfully!")


def update_student(student_list, file_path):
    if not student_list:
        print("\nNo student records available to update.")
        return

    print("\n--- Update Student Details ---")
    roll_query = input("Enter Roll Number of the student to update: ").strip()

    target_student = None
    for s in student_list:
        if str(s["roll_no"]).lower() == roll_query.lower():
            target_student = s
            break

    if not target_student:
        print(f"Student with Roll Number '{roll_query}' not found.")
        return

    print(f"\nEditing record for {target_student['name']} (Roll: {target_student['roll_no']})")
    print("1. Update Name")
    print("2. Update Department")
    print("3. Update Subject Marks")
    print("4. Cancel")
    choice = input("Enter option (1-4): ").strip()

    if choice == "1":
        new_name = input("Enter new name: ").strip()
        if new_name != "":
            target_student["name"] = new_name
            save_students_to_file(student_list, file_path)
            print("Name updated successfully.")
        else:
            print("Name cannot be empty. Update cancelled.")

    elif choice == "2":
        new_dept = input("Enter new department/class: ").strip()
        if new_dept != "":
            target_student["department"] = new_dept
            save_students_to_file(student_list, file_path)
            print("Department updated successfully.")
        else:
            print("Department cannot be empty. Update cancelled.")

    elif choice == "3":
        print("\nCurrent marks:")
        for sub, score in target_student["marks"].items():
            print(f"  * {sub}: {score}")

        sub_to_edit = input("\nEnter subject name to update (or type 'all' to re-enter all subjects): ").strip()

        if sub_to_edit.lower() == "all":
            # re-enter all marks
            new_marks = {}
            for sub in list(target_student["marks"].keys()):
                while True:
                    m_str = input(f"Enter new marks for {sub}: ").strip()
                    ok, val = validate_mark(m_str)
                    if ok:
                        new_marks[sub] = val
                        break
                    print(f"Error: {val}")
            target_student["marks"] = new_marks
        else:
            # find matching subject
            matched_sub = None
            for sub in target_student["marks"]:
                if sub.lower() == sub_to_edit.lower():
                    matched_sub = sub
                    break

            if matched_sub:
                while True:
                    m_str = input(f"Enter new marks for {matched_sub}: ").strip()
                    ok, val = validate_mark(m_str)
                    if ok:
                        target_student["marks"][matched_sub] = val
                        break
                    print(f"Error: {val}")
            else:
                print(f"Subject '{sub_to_edit}' not found in student's record.")
                return

        # recalculate totals and grades
        target_student["total"] = calculate_total(target_student["marks"])
        target_student["percentage"] = calculate_percentage(target_student["marks"])
        target_student["grade"] = calculate_grade(target_student["percentage"])
        target_student["status"] = calculate_status(target_student["percentage"])

        save_students_to_file(student_list, file_path)
        print("Marks and grade updated successfully.")

    elif choice == "4":
        print("Update cancelled.")
    else:
        print("Invalid choice.")


def delete_student(student_list, file_path):
    if not student_list:
        print("\nNo student records available to delete.")
        return

    print("\n--- Delete Student ---")
    roll_query = input("Enter Roll Number of the student to delete: ").strip()

    target_index = -1
    for i, s in enumerate(student_list):
        if str(s["roll_no"]).lower() == roll_query.lower():
            target_index = i
            break

    if target_index == -1:
        print(f"Student with Roll Number '{roll_query}' not found.")
        return

    student = student_list[target_index]
    confirm = input(f"Are you sure you want to delete {student['name']} (Roll: {student['roll_no']})? (y/n): ").strip().lower()
    if confirm in ["y", "yes"]:
        student_list.pop(target_index)
        save_students_to_file(student_list, file_path)
        print(f"Student record deleted successfully.")
    else:
        print("Deletion cancelled.")
