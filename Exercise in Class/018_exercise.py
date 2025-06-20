from datetime import datetime

"""
Exercise (18):

Testing your knowledge of datetime formats.

The following code snippet is a list of tuples.
Each tuple contains a date string and a format code.

ONLY change the format code in each tuple to match the date string (..)

The solutions are provided at 005_solution.py
"""

date_and_format_code = [
    ("20-11-2024", ".."),
    ("20/Jan/2024", ".."),
    ("20-Jan-2024", ".."),
    ("20–Jan–24 12:00:00", ".."),
    ("Date: 20–Jan–24 12:00:00 PM", ".."),
    ("20:Jan/24 12:00:00 PM", "..")
]

for date_str, format_code in date_and_format_code:
    date = datetime.strptime(date_str, format_code)
    print(date)
