"""
Exercise 20
"""

import pandas as pd
import numpy as np

# Creating a dictionary with country data
countries_data = {
    'Country': [
        'United States', 'China', 'Japan', 'Germany', 'India', 
        'United Kingdom', 'France', 'Brazil', 'Italy', 'Canada',
        'South Korea', 'Australia', 'Spain', 'Mexico', 'Indonesia',
        'Netherlands', 'Saudi Arabia', 'Turkey', 'Switzerland', 'Poland',
        'Sweden', 'Belgium', 'Nigeria', 'Argentina', 'Norway',
        'Austria', 'Thailand', 'United Arab Emirates', 'Egypt', 'Ireland',
        'Singapore', 'Malaysia', 'South Africa', 'Philippines', 'Colombia',
        'Pakistan', 'Chile', 'Vietnam', 'Bangladesh', 'New Zealand'
    ],
    'Continent': [
        'North America', 'Asia', 'Asia', 'Europe', 'Asia',
        'Europe', 'Europe', 'South America', 'Europe', 'North America',
        'Asia', 'Oceania', 'Europe', 'North America', 'Asia',
        'Europe', 'Asia', 'Asia', 'Europe', 'Europe',
        'Europe', 'Europe', 'Africa', 'South America', 'Europe',
        'Europe', 'Asia', 'Asia', 'Africa', 'Europe',
        'Asia', 'Asia', 'Africa', 'Asia', 'South America',
        'Asia', 'South America', 'Asia', 'Asia', 'Oceania'
    ],
    'Date_Joined_UN': [
        '1945-10-24', '1945-10-24', '1956-12-18', '1973-09-18', '1945-10-30',
        '1945-10-24', '1945-10-24', '1945-10-24', '1955-12-14', '1945-11-09',
        '1991-09-17', '1945-11-01', '1955-12-14', '1945-11-07', '1950-09-28',
        '1945-12-10', '1945-10-24', '1945-10-24', '2002-09-10', '1945-10-24',
        '1946-11-19', '1945-12-27', '1960-10-07', '1945-10-24', '1945-11-27',
        '1955-12-14', '1946-12-16', '1971-12-09', '1945-10-24', '1955-12-14',
        '1965-09-21', '1957-09-17', '1945-11-07', '1945-10-24', '1945-11-05',
        '1947-09-30', '1945-10-24', '1977-09-20', '1974-09-17', '1945-10-24'
    ],
    'GDP_Growth_Rate': [
        2.3, 6.1, 0.7, 1.5, 4.2,
        1.4, 1.5, 1.1, 0.3, 1.6,
        2.0, 2.2, 2.0, 2.0, 5.0,
        1.7, None, 0.9, 1.1, 4.1,
        1.2, 1.4, 2.2, -2.2, 1.2,
        1.6, 2.4, 1.7, 5.6, 5.5,
        0.7, 4.3, 0.2, 5.9, 3.3,
        1.0, 1.1, 7.0, 8.2, 2.2
    ],
    'Population_Millions': [
        331.0, 1412.0, 125.7, 83.2, 1380.0,
        67.9, 65.3, 212.6, 60.5, 38.0,
        51.7, 25.7, 47.4, 128.9, 273.5,
        17.1, 34.8, 84.3, 8.6, 37.8,
        10.4, 11.6, 206.1, 45.2, 5.4,
        9.0, 69.8, 9.9, 102.3, 4.9,
        5.7, 32.4, 59.3, 109.6, 50.9,
        220.9, 19.1, 97.3, 164.7, 5.1
    ],
    'GDP_Billions': [
        21433, 14343, 5082, 3846, None,
        2829, 2716, 1830, 1886, 1643,
        1630, 1323, 1281, 1076, 1058,
        907, 793, 760, 703, 594,
        541, 515, None, 445, 403,
        417, 505, 421, 303, 388,
        340, 336, 329, 331, 314,
        282, 282, 261, 249, 206
    ],
    'Birth_Rate': [
        11.6, 11.3, 7.3, 9.5, 17.5,
        10.7, 11.2, 13.9, 7.0, 10.1,
        6.4, 12.1, 7.4, 17.6, None,
        9.8, 14.7, 15.3, 10.5, 9.1,
        11.3, 9.9, 35.2, 16.5, 9.9,
        9.8, None, 9.8, 27.2, 11.2,
        8.9, 16.4, 19.2, 22.1, 14.8,
        27.4, 12.4, None, 18.1, 12.8
    ],
    'Internet_Users_Percent': [
        '89.4', '64.5', '93.7', '89.7', '50.0',
        '94.9', '85.6', '74.0', '74.4', '91.6',
        '96.2', '86.5', '93.2', '70.1', '53.7',
        '93.2', '95.7', '77.7', '93.1', '78.3',
        '94.5', '90.7', '42.0', '74.3', '96.5',
        '87.9', '77.8', '99.1', '57.3', '84.5',
        '88.4', '84.2', '56.2', '72.0', '65.0',
        '17.1', '82.3', '70.3', '22.0', '90.8'
    ]
}


"""
Exercise

1. Handle null values with imputing with mean.
2. Change Datatype of Internet_Users_Percent to float.
3. Change datatype of Date_Joined_UN to datetime.
4. Get Actual number of Internet Users in Millions from the Internet_Users_Percent * Population_Millions.
5. Label Internet Users based on the following criteria and add to a new column called "Internet_Users_Label":
    - High: 30 million or more
    - Medium: 10 million to 30 million
    - Low: Less than 10 million

"""
df = pd.DataFrame(countries_data)
df



