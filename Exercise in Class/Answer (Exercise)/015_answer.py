# Answer 013
# Solution will be provided after class # Exercise 013
# Instructions will be provided in class 

"""
Exercise: Make a Function with following details

name: annual_compound_interest
Input: initial_amount, interest_rate, number_of_years
Process: 
    - Loop through the number of years
    - Print the year, and the principal amount + interest
    - Update the principal amount to the principal amount + interest

Example Output:

    Initial amount: RM 1,000.00
    Interest rate: 5.0%
    Number of years: 5
    --------------------------------
    Year 1: RM 1,050.00
    Year 2: RM 1,102.50
    Year 3: RM 1,157.62
    Year 4: RM 1,215.51
    Year 5: RM 1,276.28
Return: None
"""

def annual_compound_interest(principal, interest_rate, years):
    print(f"Initial amount: RM {principal:,.2f}")
    print(f"Interest rate: {interest_rate * 100}%")
    print(f"Number of years: {years}")
    print("--------------------------------")
    for i in range(years):
        principal = principal * (1 + interest_rate) # Equivalent to 105%
        print(f"Year {i+1}: RM {principal:,.2f}")


annual_compound_interest(1000, 0.05, 5)