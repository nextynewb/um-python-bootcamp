"""
Answer for 008_exercise.py
"""

while True:
    blacklist = ['aniq', 'alia', 'muthu', 'ah chong']
    vip = ['asiah', 'fatihah', 'yee peng', 'thevan']

    name = input('What is your name?')

    if name in blacklist:
        print('You are not allowed to enter')
    elif name in vip:
        print(f'Welcome, {name}, VIP!')
    else:
        print('You are allowed to enter') 