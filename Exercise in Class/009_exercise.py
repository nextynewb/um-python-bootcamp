"""
Exercise: Do if else (Cont)

Okay - this is tougher one.

We have empty List intialized.

The program will ask for name, and if name is not in list, add the name into the list.
If the name is already in the list, print "Name already in the list"
If the name is 'all', print all the names in the list.

Example:

    all_attendees = []

    - Input: 'John'
    - Output: 'Successfully Added to List'

    - Input: 'John'
    - Output: 'Name already in the list'

    - Input: 'Ali'
    - Output: 'Successfully Added to List'

    - Input: 'all'
    - Output: 'All attendees: [John, Ali]'
"""

all_attendees = []

while True:
    name = input('Enter your name, or type "all" to see all attendees: ')

    # Continue here:
