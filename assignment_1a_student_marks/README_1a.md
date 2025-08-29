# Assignment 1a — Student Marks Analysis (Excel Automation)

**Input**: `student.xlsx` with headers: `StudentID, Name, Math, Physics, Chemistry, Biology`  
**Output**: `students.xlsx` with 2 sheets student and results:
- `Summary`: StudentID, Name, Total, Average, Grade
- `Top Performers`: top 3 in each subject

**Chart**: An **Excel** bar chart for average marks per subject (created via `openpyxl.chart`).

## Run
```bash
# (Optional) create sample input
python create_student_input.py

# Run solution
python assignment_1a.py
```