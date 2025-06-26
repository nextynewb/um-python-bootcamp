from datetime import datetime

"""
Answer (18):

Testing your knowledge of datetime formats.

The following code snippet is a list of tuples.
Each tuple contains a date string and a format code.

Format codes have been filled in to match each date string.
"""

date_and_format_code = [
    ("20-11-2024", "%d-%m-%Y"),                    # day-month-year with dashes
    ("20/Jan/2024", "%d/%b/%Y"),                   # day/month_abbreviation/year with slashes
    ("20-Jan-2024", "%d-%b-%Y"),                   # day-month_abbreviation-year with dashes
    ("20–Jan–24 12:00:00", "%d–%b–%y %H:%M:%S"),   # day–month_abbreviation–year_2digit with en-dash and 24hr time
    ("Date: 20–Jan–24 12:00:00 PM", "Date: %d–%b–%y %I:%M:%S %p"),  # prefix + day–month_abbreviation–year_2digit with 12hr time
    ("20:Jan/24 12:00:00 PM", "%d:%b/%y %I:%M:%S %p")               # day:month_abbreviation/year_2digit with 12hr time
]

print("=== DATETIME FORMAT PARSING RESULTS ===")
for i, (date_str, format_code) in enumerate(date_and_format_code, 1):
    try:
        date = datetime.strptime(date_str, format_code)
        print(f"{i}. '{date_str}' -> {date}")
        print(f"   Format: '{format_code}'")
        print()
    except ValueError as e:
        print(f"{i}. ERROR: '{date_str}' with format '{format_code}'")
        print(f"   Error: {e}")
        print()

"""
Format Code Reference:
%d - Day of the month as a zero-padded decimal (01-31)
%m - Month as a zero-padded decimal (01-12)  
%Y - Year with century as a decimal number (e.g., 2024)
%y - Year without century as a zero-padded decimal (00-99)
%b - Month as abbreviated name (Jan, Feb, etc.)
%H - Hour (24-hour clock) as a zero-padded decimal (00-23)
%I - Hour (12-hour clock) as a zero-padded decimal (01-12)
%M - Minute as a zero-padded decimal (00-59)
%S - Second as a zero-padded decimal (00-59)
%p - AM or PM
""" 