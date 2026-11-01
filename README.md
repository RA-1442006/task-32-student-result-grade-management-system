# Task 32: Student Result & Grade Management System

A Python command-line application developed as part of the **Veda Technology Internship**. This project helps teachers and administrators manage student academic records, calculate percentages and grades automatically, perform statistical summaries of class performance, and persist all data using a local JSON file.

---

## 📌 Project Overview & Objective

The objective of this project is to build an interactive, menu-driven CLI application using core Python fundamentals without relying on any third-party libraries. It replaces manual grade sheet calculations and paper record-keeping with a reliable, validated command-line tool.

Key goals:
- Practice core Python constructs: loops, conditionals, functions, lists, and dictionaries.
- Implement robust input validation (prevent invalid marks, non-numeric values, duplicate roll numbers).
- Organize code into clean, modular files for separation of concerns.
- Persist data safely between sessions using Python's standard `json` module.

---

## 🚀 Features

1. **Interactive Menu Loop**: A clean terminal interface that loops continuously until you choose to exit.
2. **Add Student Records**:
   - Stores roll number, student name, class/department, and any number of subjects with marks.
   - Prevents duplicate roll numbers and empty fields.
3. **Data Validation**:
   - Ensures marks are numeric and strictly within the `0 to 100` range.
   - Prevents empty inputs or negative values.
4. **Automatic Calculations**:
   - Computes total marks and percentage.
   - Assigns grades based on percentage criteria:
     - **A+**: 90% and above
     - **A**: 80% to 89.99%
     - **B**: 70% to 79.99%
     - **C**: 60% to 69.99%
     - **D**: 50% to 59.99%
     - **F**: Below 50%
   - Determines **Pass / Fail** status (Pass if percentage is 50% or above).
5. **View All Students**: Displays all records in a formatted tabular layout.
6. **Search Functionality**: Supports partial, case-insensitive search by both roll number and student name, displaying a complete breakdown of subject marks.
7. **Update Records**: Easily modify student names, departments, or individual subject marks with automatic grade recalculation.
8. **Delete Records**: Safe removal of student entries with a confirmation prompt.
9. **Class Performance Summary**:
   - Class average percentage.
   - Highest and lowest scorers with roll numbers and grades.
   - Overall pass percentage and pass/fail counts.
   - Grade distribution breakdown (count of A+, A, B, C, D, F).
   - Subject-wise average marks across all students.
10. **Data Persistence**: Automatically reads and writes all records to `data/students.json`.

---

## 🛠️ Tools & Technologies Used

- **Python 3.8+**: Core programming language (only standard libraries: `os`, `json`).
- **VS Code**: Code editor, integrated terminal, and debugging.
- **Git**: Local version control with incremental commits.
- **GitHub**: Remote repository hosting and project showcase.

---

## 📁 Folder Structure

```text
task-32-student-result-grade-management-system/
 ├── main.py                          # Program entry point and menu navigation
 ├── student_manager.py               # Add, update, delete, view, search, and JSON handling
 ├── grade_calculator.py              # Input validation, total, percentage, and grade logic
 ├── summary.py                       # Performance analytics and class statistics
 ├── data/
 │    └── students.json               # Persistent JSON storage with 5 sample students
 ├── sample_output/
 │    └── sample_output.txt          # Real captured output of a complete demo run
 ├── README.md                        # Project documentation and summary
 └── .gitignore                       # Git ignore rules for Python and editor caches
```

---

## 💻 How to Run

### Prerequisites
Make sure Python 3.8 or newer is installed on your computer:
```bash
python --version
```

### Steps to Run
1. Clone or navigate to the project directory:
   ```bash
   cd task-32-student-result-grade-management-system
   ```

2. Run the application using Python:
   ```bash
   python main.py
   ```

3. Follow the numbered on-screen menu to manage student records. All changes will be saved automatically to `data/students.json`.

---

## 📊 Sample Output Preview

Below is a snippet of the table view and class performance summary:

```text
============================================================================================
Roll No    Name                   Department             Total    Percentage   Grade    Status  
--------------------------------------------------------------------------------------------
101        Rahul Sharma           Computer Science       429.00   85.80%       A        Pass    
102        Priya Patel            Information Technology 460.00   92.00%       A+       Pass    
103        Amit Kumar             Electronics            315.00   63.00%       C        Pass    
104        Sneha Reddy            Computer Science       379.00   75.80%       B        Pass    
105        Vikram Singh           Mechanical             225.00   45.00%       F        Fail    
============================================================================================
Total Students: 5

=======================================================
           CLASS PERFORMANCE SUMMARY
=======================================================
Total Enrolled Students : 5
Class Average Percentage: 72.32%
-------------------------------------------------------
Highest Scorer          : Priya Patel (Roll: 102)
  Score                 : 92.00% (Total: 460.00, Grade: A+)
Lowest Scorer           : Vikram Singh (Roll: 105)
  Score                 : 45.00% (Total: 225.00, Grade: F)
-------------------------------------------------------
Students Passed         : 4
Students Failed         : 1
Overall Pass Percentage : 80.00%
-------------------------------------------------------
Grade Distribution:
  Grade A+ : 1 student(s)
  Grade A  : 1 student(s)
  Grade B  : 1 student(s)
  Grade C  : 1 student(s)
  Grade D  : 0 student(s)
  Grade F  : 1 student(s)
-------------------------------------------------------
Subject-wise Averages:
  * Chemistry           : 69.60 (from 5 students)
  * Computer Science    : 75.20 (from 5 students)
  * English             : 76.20 (from 5 students)
  * Mathematics         : 72.20 (from 5 students)
  * Physics             : 68.80 (from 5 students)
=======================================================
```

The full terminal transcript with add, update, search, view, and validation flows is saved in [sample_output/sample_output.txt](sample_output/sample_output.txt).

---

## 🎓 What I Learned

During this project under the Veda Technology Internship, I gained hands-on experience in:
1. **Modular Code Structure**: Dividing a project into multiple Python modules (`main.py`, `student_manager.py`, `grade_calculator.py`, `summary.py`) rather than putting everything into a single file, which makes code much easier to read and maintain.
2. **Defensive Programming & Input Validation**: Validating user inputs before performing calculations so that invalid marks, non-numeric values, or duplicate roll numbers don't crash the program.
3. **Working with Nested Dictionaries & Lists**: Managing student records where each student is represented as a dictionary containing nested dictionaries for subjects and scores.
4. **Data Persistence with JSON**: Using Python's `json` module to load and save records dynamically so data isn't lost when the application closes.
5. **Git Version Control**: Initializing Git repositories, structuring meaningful commit messages, and managing project repositories on GitHub.
