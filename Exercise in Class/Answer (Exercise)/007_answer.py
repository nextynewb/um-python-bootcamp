"""
Answer for 007_exercise.py
"""

blacklist = ['Ammar', 'John', 'Jane', 'Jim', 'Jill']

name = input('Enter your name: ')
if name in blacklist:
    print('You are not allowed to enter!')
else:
    print('You are allowed to enter!') 