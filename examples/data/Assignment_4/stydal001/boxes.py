# Dalise Steynfaard
# STYDAL001
# Assignment 4, question 1
# 01-04-2014

def print_square():
    print('*'*5 + '\n' + '*   *\n'*3 + '*'*5)

def get_rectangle(width, height):
    return ('*'*width + '\n' + ('*' + ' '*(width-2) + '*\n')*(height-2) + '*'*width)

def print_rectangle(width, height):
    print(get_rectangle(width,height))