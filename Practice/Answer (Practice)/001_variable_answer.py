"""
Answer for 001_variable.py
"""

# (1): Create variables for economic data
country = 'Indonesia'
gdp = 1417.4
currency = 'IDR'
year = 2023

# (2): Check the type of each variable
print(type(country))   # <class 'str'>
print(type(gdp))       # <class 'float'>
print(type(currency))  # <class 'str'>
print(type(year))      # <class 'int'>

# (3): Variable concatenation
print(f"{country} GDP in {year} was {gdp} {currency}")

# (4): Convert salary variable to 20000 using string manipulation
salary = "$20k USD"
salary_value = int(salary.replace("$", "").replace("k", "000").split()[0])
print(salary_value)  # Output: 20000 