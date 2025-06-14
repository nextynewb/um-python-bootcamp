"""
Answer for 002_list.py
"""

# (1): Create a list of countries
countries = ['Malaysia', 'Singapore', 'Indonesia']
print(countries)

# (2): Access the second item of the list
print(countries[1])  # Output: Singapore

# (3): Add Malawi to the List
countries.append('Malawi')
print(countries)

# (4): Remove Malaysia from the List
countries.remove('Malaysia')
print(countries)

# (5): Sort the List in Descending Order
countries.sort(reverse=True)
print(countries)

