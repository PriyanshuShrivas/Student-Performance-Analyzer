"""Matplotlib charts for student performance."""
from pathlib import Path
import matplotlib.pyplot as plt
from data_manager import SUBJECTS


def create_charts(data, subject_averages, report_dir):
    report_dir = Path(report_dir)
    report_dir.mkdir(parents=True, exist_ok=True)

    # Bar chart: average marks in each subject.
    plt.figure(figsize=(8, 5))
    bars = plt.bar(subject_averages.index, subject_averages.values,
                   edgecolor="black")
    plt.title("Subject-wise Average Marks")
    plt.xlabel("Subjects")
    plt.ylabel("Average Marks (out of 100)")
    plt.ylim(0, 110)
    plt.grid(axis="y", linestyle="--", alpha=0.4)

    for bar, value in zip(bars, subject_averages.values):
        plt.text(bar.get_x() + bar.get_width() / 2,
                 bar.get_height() + 2, f"{value:.2f}",
                 ha="center", va="bottom")

    plt.tight_layout()
    bar_path = report_dir / "subject_average_bar_chart.png"
    plt.savefig(bar_path, dpi=150)
    print(f"\nBar chart saved: {bar_path}")
    plt.show()
    plt.close()

    # Histogram: distribution of percentages.
    plt.figure(figsize=(8, 5))
    plt.hist(data["Percentage"], bins=5, edgecolor="black", rwidth=0.9)
    plt.title("Distribution of Student Percentages")
    plt.xlabel("Percentage")
    plt.ylabel("Number of Students")
    plt.grid(axis="y", linestyle="--", alpha=0.4)
    plt.tight_layout()
    histogram_path = report_dir / "student_percentage_histogram.png"
    plt.savefig(histogram_path, dpi=150)
    print(f"Histogram saved: {histogram_path}")
    plt.show()
    plt.close()
