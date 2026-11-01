# grade_calculator.py
# functions for validating input and calculating marks, percentages and grades

def validate_roll_no(roll_no, student_list):
    # roll number should not be empty
    if not roll_no or roll_no.strip() == "":
        return False, "Roll number cannot be empty."

    roll_clean = roll_no.strip()
    # check for duplicates in the list
    for student in student_list:
        if str(student["roll_no"]).lower() == roll_clean.lower():
            return False, f"Roll number '{roll_clean}' already exists."

    return True, roll_clean


def validate_mark(mark_text):
    # check empty mark
    if not mark_text or mark_text.strip() == "":
        return False, "Mark cannot be empty. Please enter a number."

    # check if it is a number
    try:
        mark = float(mark_text)
    except ValueError:
        return False, "Invalid input. Marks must be a number."

    # range check 0 to 100
    if mark < 0 or mark > 100:
        return False, "Marks must be between 0 and 100."

    return True, mark


def calculate_total(marks_dict):
    total = 0.0
    for subject, score in marks_dict.items():
        total += score
    return round(total, 2)


def calculate_percentage(marks_dict):
    if not marks_dict or len(marks_dict) == 0:
        return 0.0
    total = calculate_total(marks_dict)
    percentage = total / len(marks_dict)
    return round(percentage, 2)


def calculate_grade(percentage):
    # grade logic based on percentage
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"


def calculate_status(percentage):
    if percentage >= 50:
        return "Pass"
    else:
        return "Fail"
