# Student Performance Analyzer — PS No. 87

A Python 3 mini-project using Pandas, NumPy and Matplotlib.

## Folder structure

- `main.py` — application menu and program entry point
- `data_manager.py` — CSV loading, validation and grade calculation
- `analyzer.py` — student result table and class statistics
- `visualizer.py` — bar chart and histogram generation
- `data/students.csv` — input student dataset
- `reports/` — generated chart images
- `requirements.txt` — Python package list

## Setup

Open this folder in VS Code, then open Terminal > New Terminal.

```bash
python -m pip install -r requirements.txt
python main.py
```

If `python` is not recognized on Windows, try `py main.py`.

## CSV format

The CSV must contain these columns:

`Name,Maths,Physics,Chemistry`

Each subject mark must be between 0 and 100. Invalid student rows are skipped.

## Menu

1. Display Student Results
2. Display Class Statistics and Charts
3. Exit

The charts are saved in the `reports` folder.
