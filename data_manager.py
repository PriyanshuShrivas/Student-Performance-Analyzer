"""CSV loading and input validation."""
from pathlib import Path
import numpy as np
import pandas as pd

SUBJECTS = ["Maths", "Physics", "Chemistry"]
REQUIRED_COLUMNS = ["Name"] + SUBJECTS


def load_student_data(csv_file):
    csv_file = Path(csv_file)

    if not csv_file.exists():
        print(f"\nError: {csv_file} was not found.")
        print("Make sure students.csv is inside the data folder.")
        return pd.DataFrame()

    try:
        raw = pd.read_csv(csv_file, dtype=str, keep_default_na=False)
    except (pd.errors.EmptyDataError, pd.errors.ParserError, OSError) as error:
        print(f"\nCould not read CSV: {error}")
        return pd.DataFrame()

    missing = [col for col in REQUIRED_COLUMNS if col not in raw.columns]
    if missing:
        print("CSV is missing required columns:", ", ".join(missing))
        print("Required columns:", ", ".join(REQUIRED_COLUMNS))
        return pd.DataFrame()

    valid_rows = []
    for _, row in raw.iterrows():
        name = row["Name"].strip()
        if not name:
            print("Invalid student name. Row skipped.")
            continue

        marks = {}
        invalid = None
        for subject in SUBJECTS:
            value = row[subject].strip()
            try:
                mark = float(value)
                if not np.isfinite(mark) or not 0 <= mark <= 100:
                    raise ValueError
                marks[subject] = mark
            except (ValueError, TypeError):
                invalid = (subject, value or "(blank)")
                break

        if invalid:
            subject, value = invalid
            print(f"Invalid marks for {name} in {subject}: '{value}'. Row skipped.")
            continue

        total = sum(marks.values())
        percentage = total / 300 * 100
        grade = calculate_grade(percentage)

        valid_rows.append({
            "Name": name,
            **marks,
            "Total": total,
            "Percentage": percentage,
            "Grade": grade
        })

    return pd.DataFrame(valid_rows)


def calculate_grade(percentage):
    if percentage >= 90:
        return "A"
    if percentage >= 75:
        return "B"
    if percentage >= 60:
        return "C"
    if percentage >= 40:
        return "D"
    return "F"
