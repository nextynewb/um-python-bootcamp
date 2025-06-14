"""
Answer for 004_list_and_dictionary.py
"""

countries = [
    {
        "name": "Indonesia",
        "capital": "Jakarta",
        "gdp_billion_usd": 1186.5,
        "population_million": 273.5
    },
    {
        "name": "Singapore", 
        "capital": "Singapore",
        "gdp_billion_usd": 397.3,
        "population_million": 5.9
    },
    {
        "name": "Malaysia",
        "capital": "Kuala Lumpur", 
        "gdp_billion_usd": 372.7,
        "population_million": 32.7
    },
    {
        "name": "Thailand",
        "capital": "Bangkok",
        "gdp_billion_usd": 505.9,
        "population_million": 69.8
    }
]

# (1): Print the second item of the list
print(countries[1])  # Output: Singapore's info

# (2): Print the population_million of the second item
print(countries[1]['population_million'])  # Output: 5.9

# (3): Print the name of the second item
print(countries[1]['name'])  # Output: Singapore 