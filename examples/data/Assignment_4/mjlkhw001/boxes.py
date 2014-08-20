# Module to create boxes of stars
# Khwezi Majola
# MJLKHW001
# 31 March 2014

def print_square():
    print('*' * 5)
    for i in range(3):
        print('*' + ' ' * 3 + '*')
    print('*' * 5)

def print_rectangle(width, height):
    print('*' * width)
    for i in range(height - 2):
        print('*' + ' ' * (width-2) + '*')
    print('*' * width)

def get_rectangle(width, height): 
    x = ''
    x += '*' * width + '\n'
    for i in range(height - 2):
            x += ('*' + ' ' * (width-2) + '*') + '\n'
    x += '*' * width + '\n'
    return x