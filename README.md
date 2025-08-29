
## Repo Structure

```
viglobal/
├─ assignment_1a_student_marks/
│  ├─ assignment_1a.py
│  ├─ create_student_input.py
│  └─ README_1a.md
├─ assignment_1b_polygon_geometry/
│  ├─ assignment_1b.py
│  └─ README_1b.md
├─ assignment_2_room_tiling/
│  ├─ assignment_2.py
│  └─ README_2.md
├─ assignment_3_triangle_pyramid/
│  ├─ assignment_3.py
│  └─ README_3.md
├─ interview_explainer.md
├─ requirements.txt
└─ .gitignore
```

## Quickstart

1) Create & activate venv (recommended)
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
```

2) Install deps
```bash
pip install -r requirements.txt
```

3) Run each task from its folder (examples below).

### 1a — Student Marks Analysis (Excel Automation)
```bash
cd assignment_1a_student_marks
# (Optional) generate example input Excel
python create_student_input.py
# Run solution (reads student.xlsx, writes students.xlsx with student and results sheets + Excel bar chart)
python assignment_1a.py
```

### 1b — Polygon Geometry (Vector Algebra + Plot)
```bash
cd assignment_1b_polygon_geometry
python assignment_1b.py
```

### 2 — Room Tiling with Squares (Spiral Fill + Plot)
```bash
cd assignment_2_room_tiling
python assignment_2.py --width 20 --height 16
```

### 3 — Pyramid Building with Triangles (Plot)
```bash
cd assignment_3_triangle_pyramid
python assignment_3.py --size 1.0 --depth 5
```
