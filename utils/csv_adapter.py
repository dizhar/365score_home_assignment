import csv
import os

class CSVAdapter:
    """Adapter for reading test data from a CSV file."""

    def __init__(self, file_name="test_data.csv", base_path="tests/data/"):
        file_path = os.path.join(base_path, file_name)
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"CSV file not found: {file_path}")
        self.file_path = file_path

    def read_data(self):
        """Read data from CSV and return as a list of dictionaries."""
        with open(self.file_path, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            return [row for row in reader]
