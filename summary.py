# summary.py
# module to calculate and display class performance metrics

def display_performance_summary(student_list):
    if not student_list or len(student_list) == 0:
        print("\nNo student records available to generate summary.")
        return

    print("\n" + "=" * 55)
    print("           CLASS PERFORMANCE SUMMARY")
    print("=" * 55)

    total_students = len(student_list)
    print(f"Total Enrolled Students : {total_students}")

    # 1. Class average percentage
    total_percentage_sum = 0.0
    for s in student_list:
        total_percentage_sum += s.get("percentage", 0.0)
    class_average = total_percentage_sum / total_students
    print(f"Class Average Percentage: {class_average:.2f}%")

    # 2. Highest and lowest scorer
    highest_student = student_list[0]
    lowest_student = student_list[0]

    for s in student_list:
        if s.get("percentage", 0) > highest_student.get("percentage", 0):
            highest_student = s
        if s.get("percentage", 0) < lowest_student.get("percentage", 0):
            lowest_student = s

    print("-" * 55)
    print(f"Highest Scorer          : {highest_student['name']} (Roll: {highest_student['roll_no']})")
    print(f"  Score                 : {highest_student.get('percentage', 0):.2f}% (Total: {highest_student.get('total', 0):.2f}, Grade: {highest_student.get('grade', '')})")

    print(f"Lowest Scorer           : {lowest_student['name']} (Roll: {lowest_student['roll_no']})")
    print(f"  Score                 : {lowest_student.get('percentage', 0):.2f}% (Total: {lowest_student.get('total', 0):.2f}, Grade: {lowest_student.get('grade', '')})")

    # 3. Pass / Fail count and Pass Percentage
    passed_count = 0
    failed_count = 0
    for s in student_list:
        if s.get("status", "") == "Pass":
            passed_count += 1
        else:
            failed_count += 1

    pass_percentage = (passed_count / total_students) * 100
    print("-" * 55)
    print(f"Students Passed         : {passed_count}")
    print(f"Students Failed         : {failed_count}")
    print(f"Overall Pass Percentage : {pass_percentage:.2f}%")

    # 4. Grade distribution
    grades_count = {"A+": 0, "A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
    for s in student_list:
        g = s.get("grade", "F")
        if g in grades_count:
            grades_count[g] += 1
        else:
            grades_count[g] = 1

    print("-" * 55)
    print("Grade Distribution:")
    for grade_label in ["A+", "A", "B", "C", "D", "F"]:
        count = grades_count.get(grade_label, 0)
        print(f"  Grade {grade_label:<2} : {count} student(s)")

    # 5. Subject-wise average
    subject_totals = {}
    subject_counts = {}

    for s in student_list:
        marks = s.get("marks", {})
        for subj, val in marks.items():
            if subj not in subject_totals:
                subject_totals[subj] = 0.0
                subject_counts[subj] = 0
            subject_totals[subj] += val
            subject_counts[subj] += 1

    print("-" * 55)
    print("Subject-wise Averages:")
    if subject_totals:
        for subj in sorted(subject_totals.keys()):
            avg = subject_totals[subj] / subject_counts[subj]
            print(f"  * {subj:<20}: {avg:.2f} (from {subject_counts[subj]} students)")
    else:
        print("  No subject data available.")

    print("=" * 55 + "\n")
