import csv
import os
import pandas as pd

CSV_FILE = "progress_data.csv"

def save_progress_to_csv(entry):
    file_exists = os.path.isfile(CSV_FILE)

    with open(CSV_FILE, "a", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["date", "weight", "workout_done"]
        )

        if not file_exists:
            writer.writeheader()

        writer.writerow(entry)

def load_progress():
    if os.path.isfile(CSV_FILE):
        return pd.read_csv(CSV_FILE, parse_dates=["date"])
    return pd.DataFrame()
