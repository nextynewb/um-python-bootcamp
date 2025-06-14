"""
Answer for 004_exercise.py
"""

countries = {
    'Malaysia':{
        'capital': 'Kuala Lumpur',
        'population': 32000000,
        'currency': 'Malaysia Ringgit'
    },
    'Singapore':{
        'capital': 'Singapore',
        'population': 5600000,
        'currency': 'Singapore Dollar'
    }
}

# Question (1): Print Malaysia info
print(countries['Malaysia'])

# Question (2): Print Capital of Malaysia
print(countries['Malaysia']['capital'])

# Question (3): Print Population of Singapore
print(countries['Singapore']['population'])

# Question (4): Print total population of both countries (Use arithmetic operator!)
total_population = countries['Malaysia']['population'] + countries['Singapore']['population']
print(total_population) 