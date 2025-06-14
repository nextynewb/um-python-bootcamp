"""
Answer for 005_if_else.py
"""

# (1): Basic if-else statement
inflation_rate = 4.5
if inflation_rate > 5:
    print("High Inflation")
else:
    print("Low Inflation")

# (2): If-elif-else statement
inflation_rate = 5.0
if inflation_rate > 5:
    print("High Inflation")
elif inflation_rate < 5:
    print("Low Inflation")
else:
    print("Medium Inflation")

# (3): Nested if-else statement
inflation_rate = 4.5
unemployment_rate = 6.5
if inflation_rate > 5 and unemployment_rate < 7:
    print("High Inflation and Low Unemployment")
elif inflation_rate < 5 and unemployment_rate > 7:
    print("Low Inflation and High Unemployment")
elif inflation_rate < 5 and unemployment_rate < 7:
    print("Low Inflation and Low Unemployment!") 