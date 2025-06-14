"""
Answer for 003_dictionary.py
"""

# (1): Create a dictionary of countries with key as country name and value as capital city
countries_info = {
    'Malaysia': 'Kuala Lumpur',
    'Indonesia': 'Jakarta',
    'Singapore': 'Singapore'
}
print(countries_info)

# (2): Access the value of the key 'Indonesia'
print(countries_info['Indonesia'])  # Output: Jakarta

# (3): Add new country with key of Thailand, and value of Bangkok
countries_info['Thailand'] = 'Bangkok'
print(countries_info)

# (4): Remove Malaysia from dictionary
countries_info.pop('Malaysia')
print(countries_info)

# (5): Update the value of the key in 'Indonesia'
countries_info['Indonesia'] = 'Nusantara'
print(countries_info) 