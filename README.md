
# Student Performance Analyzer

A Python-based application that analyzes student academic performance using CSV datasets. It calculates student results, assigns grades, displays class statistics, and generates graphical reports.

## Features

- Load student records from CSV files.
- Calculate total marks and percentages.
- Automatically assign grades.
- Validate student names and marks.
- Skip invalid student records.
- Calculate class statistics:
  - Mean
  - Median
  - Mode
  - Population standard deviation
  - Topper
- Calculate subject-wise average marks.
- Generate performance charts using Matplotlib.
- Run four predefined test cases.

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- CSV

## Project Structure

```text
Student_Performance_Analyzer/
│
├── main.py
├── data_manager.py
├── analyzer.py
├── visualizer.py
├── README.md
├── requirements.txt
│
├── data/
│   └── students.csv
│
├── testcases/
│   ├── test_case_1_normal.csv
│   ├── test_case_2_boundary.csv
│   ├── test_case_3_invalid.csv
│   └── test_case_4_statistics.csv
│
└── reports/
    ├── subject_average_bar_chart.png
    └── student_percentage_histogram.png
```

## Installation

1. Install Python on your computer.
2. Open the project folder in VS Code.
3. Open the integrated terminal.
4. Install the required packages:

```bash
python -m pip install -r requirements.txt
```

## How to Run

Execute the following command:

```bash
python main.py
```

## Application Menu

| Option | Function |
|---|---|
| 1 | Display student results from the main dataset |
| 2 | Display class statistics and generate charts |
| 3 | Run normal input test case |
| 4 | Run boundary input test case |
| 5 | Run invalid input test case |
| 6 | Run statistics test case |
| 7 | Exit the application |

## Grading System

Grades are assigned according to the following percentage ranges:

| Percentage | Grade |
|---|---|
| 90–100 | A |
| 75–89.99 | B |
| 60–74.99 | C |
| 40–59.99 | D |
| Below 40 | F |

## Input CSV Format

The CSV file must contain the following columns:

```csv
Name,Maths,Physics,Chemistry
Aman,80,70,90
Riya,60,65,70
Karan,40,35,50
```

Each subject mark must be a valid number between 0 and 100.

Records containing invalid names or marks are skipped during processing.

## Test Cases

The project includes four test datasets:

1. **Normal Input:** Tests ordinary student records.
2. **Boundary Input:** Tests marks at grade boundaries and score limits.
3. **Invalid Input:** Tests missing names, invalid values, negative marks and marks above 100.
4. **Statistics:** Tests class-level calculations using multiple student records.

## Generated Reports

The application generates two graphical reports in the `reports/` directory:

- `subject_average_bar_chart.png` – Displays average marks for each subject.
- `student_percentage_histogram.png` – Displays the distribution of student percentages.

## Author

Developed as a Python academic project to demonstrate data handling, data analysis, input validation and visualization.
