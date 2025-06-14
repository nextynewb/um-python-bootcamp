"""
Answer for 009_exercise.py
"""

all_attendees = []

while True:
    name = input('Enter your name, or type "all" to see all attendees: ')
    if name == 'all':
        print('All attendees:', all_attendees)
    elif name not in all_attendees:
        all_attendees.append(name)
        print('Successfully Added to List')
    else:
        print('Name already in the list') 