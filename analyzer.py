
"""Functions for displaying student results and class statistics."""

import numpy as np
from data_manager import SUBJECTS
from visualizer import create_charts


def display_results(data):
    if data.empty:
        print("\nNo valid student records available.")
        return

    print("\n" + "=" * 72)
    print("                         STUDENT RESULTS")
    print("=" * 72)

    result = data[["Name", "Total", "Percentage", "Grade"]].copy()

    result["Total"] = result["Total"].map(
        lambda value: f"{value:g}"
    )

    result["Percentage"] = result["Percentage"].map(
        lambda value: f"{value:.2f}%"
    )

    print(result.to_string(index=False))
    print("=" * 72)


def display_statistics(data, report_dir):
    if data.empty:
        print("\nNo valid student records available for statistics.")
        return

    # Extract student percentages using NumPy
    percentages = data["Percentage"].to_numpy(dtype=float)

    # Calculate class statistics
    mean_value = np.mean(percentages)
    median_value = np.median(percentages)
    std_value = np.std(percentages, ddof=0)

    # Calculate mode using Pandas
    mode_values = data["Percentage"].mode()

    # Find topper
    topper = data.loc[data["Percentage"].idxmax()]

    # Calculate subject-wise averages
    subject_averages = data[SUBJECTS].mean()

    # Display statistics
    print("\n" + "=" * 60)
    print("                    CLASS STATISTICS")
    print("=" * 60)

    print(f"Mean Percentage      : {mean_value:.2f}")
    print(f"Median Percentage    : {median_value:.2f}")

    if data["Percentage"].value_counts().max() == 1:
        print("Mode Percentage      : No mode")
    else:
        modes = ", ".join(f"{value:.2f}" for value in mode_values)
        print(f"Mode Percentage      : {modes}")

    print(f"Std Dev (Population) : {std_value:.2f}")

    print(
        f"Topper               : "
        f"{topper['Name']} ({topper['Percentage']:.2f}%)"
    )

    print("\nSubject-wise Averages:")

    for subject, average in subject_averages.items():
        print(f"{subject:<15}: {average:.2f}")

    print("=" * 60)

    create_charts(data, subject_averages, report_dir)
