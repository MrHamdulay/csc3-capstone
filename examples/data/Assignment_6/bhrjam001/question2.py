# James Behr
# 2014-04-23
# Assignment 6 Question 2

import math

def entervector(letter):
    '''Generate a three element tuple user input'''
    print('Enter vector ', letter, ':', sep='')
    inputstr = input()
    # Split the input string, cast each element to int and store as tuple
    vector = tuple(int(i) for i in inputstr.split()) 
    return vector

def norm(v):
    '''Using a list comprehension, determine the norm sqrt(a^2 + b^2 + ...)'''
    return math.sqrt(sum([v[i] ** 2 for i in range(0, len(v))]))
    
# Get vectors from user input
a = entervector('A')
b = entervector('B')

# Do A + B
print('A+B', '=', [a[i] + b[i] for i in range(0, 3)])

# Do A.B
print('A.B', '=', sum([a[i] * b[i] for i in range(0, 3)]))

# Do |A| and |B|
formatstr = '{:0.2f}'
print('|A|', '=', formatstr.format(round(norm(a), 2)))
print('|B|', '=', formatstr.format(round(norm(b), 2)))