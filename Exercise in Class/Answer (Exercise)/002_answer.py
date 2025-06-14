"""
Answer for 002_exercise.py
"""

salary_str = "$20k"

# Convert salary string to integer
normalized_salary = int(salary_str.replace("$", "").replace("k", "000"))
print(normalized_salary)  # Output: 20000 