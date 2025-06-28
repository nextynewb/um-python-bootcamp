from datetime import datetime


# Create a list of dictionaries with birth rate data for each month using datetime format
birth_rate_data = [
    {"date": "01-01-2024", "births": 1250},
    {"date": "01-02-2024", "births": 1180},
    {"date": "01-03-2024", "births": 1320},
    {"date": "01-04-2024", "births": 1280},
    {"date": "01-05-2024", "births": 1350},
    {"date": "01-06-2024", "births": 1420},
    {"date": "01-07-2024", "births": 1380},
    {"date": "01-08-2024", "births": 1450},
    {"date": "01-09-2024", "births": 1400},
    {"date": "01-10-2024", "births": 1360},
    {"date": "01-11-2024", "births": 1290},
    {"date": "01-12-2024", "births": 1500},
    {"date": "01-01-2025", "births": 1280},
    {"date": "01-02-2025", "births": 1210},
    {"date": "01-03-2025", "births": 1350},
    {"date": "01-04-2025", "births": 1310},
    {"date": "01-05-2025", "births": 1380},
    {"date": "01-06-2025", "births": 1450},
    {"date": "01-07-2025", "births": 1410},
    {"date": "01-08-2025", "births": 1480},
    {"date": "01-09-2025", "births": 1430},
    {"date": "01-10-2025", "births": 1390},
    {"date": "01-11-2025", "births": 1320},
    {"date": "01-12-2025", "births": 1530}
]

"""

1. Loop through the birth_rate_data and convert the date to datetime format
2. Create a new column called 'month' that contains the month of the date
3. Print the data
"""


datetime_format = "X" # Fill the correct format code

for data in birth_rate_data:
    date = datetime.strptime(data['date'], datetime_format)
    month = date.month

    # Add the month to the data
    
    # Print the data



