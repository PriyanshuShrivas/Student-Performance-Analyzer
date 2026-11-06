
"""Main entry point for Student Performance Analyzer."""

from pathlib import Path
from data_manager import load_student_data
from analyzer import display_results, display_statistics


# Project folders
BASE_DIR = Path(__file__).resolve().parent
CSV_FILE = BASE_DIR / "data" / "students.csv"
TESTCASE_DIR = BASE_DIR / "testcases"
REPORT_DIR = BASE_DIR / "reports"

REPORT_DIR.mkdir(exist_ok=True)


# Test case files
TEST_CASES = {
    "3": ("Test Case 1 - Normal Input", "test_case_1_normal.csv"),
    "4": ("Test Case 2 - Boundary Input", "test_case_2_boundary.csv"),
    "5": ("Test Case 3 - Invalid Input", "test_case_3_invalid.csv"),
    "6": ("Test Case 4 - Statistics", "test_case_4_statistics.csv")
}


def run_test_case(title, filename):
    """Load and analyse a selected test case."""

    print("\n" + "=" * 60)
    print(title.upper())
    print("=" * 60)

    csv_path = TESTCASE_DIR / filename

    data = load_student_data(csv_path)

    print("\nSTUDENT RESULTS:")
    display_results(data)

    print("\nCLASS STATISTICS:")
    display_statistics(data, REPORT_DIR)


def main():
    print("=" * 60)
    print("             STUDENT PERFORMANCE ANALYZER")
    print("=" * 60)

    while True:
        print("\nMAIN MENU")
        print("-" * 40)
        print("1. Display Student Results (Main Dataset)")
        print("2. Display Class Statistics and Charts")
        print("3. Run Test Case 1 - Normal Input")
        print("4. Run Test Case 2 - Boundary Input")
        print("5. Run Test Case 3 - Invalid Input")
        print("6. Run Test Case 4 - Statistics")
        print("7. Exit")
        print("-" * 40)

        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            data = load_student_data(CSV_FILE)
            display_results(data)

        elif choice == "2":
            data = load_student_data(CSV_FILE)
            display_statistics(data, REPORT_DIR)

        elif choice in TEST_CASES:
            title, filename = TEST_CASES[choice]
            run_test_case(title, filename)

        elif choice == "7":
            print("\nThank you for using Student Performance Analyzer!")
            break

        else:
            print("\nInvalid choice. Please enter a number between 1 and 7.")


if __name__ == "__main__":
    main()
