"""
Answer for 005_exercise.py
"""

countries = {
    'Malaysia':{
        'capital': 'Kuala Lumpur',
        'population': 32000000,
        'currency': 'Malaysia Ringgit',
        'languages': ['Malay', 'English', 'Chinese']
    },
    'Singapore':{
        'capital': 'Singapore',
        'population': 5600000,
        'currency': 'Singapore Dollar',
        'languages': ['English', 'Chinese', 'Malay']
    }
}

# Question (1): Print first item of languages in Malaysia
print(countries['Malaysia']['languages'][0])  # Output: Malay

# Question (2): Print number of languages in Singapore (Use len())
print(len(countries['Singapore']['languages']))  # Output: 3 