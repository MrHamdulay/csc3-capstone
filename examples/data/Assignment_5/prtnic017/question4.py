# Student Number: PRTNIC017
# Date: 4/13/14
# Draw a graph of any given function using ASCII characters
import math

scale = 1
size = 10
function = input('Enter a function f(x):\n')

for y in range(size * scale, (-1 - size) * scale, -1 * scale):
    for x in range(-size * scale, (size + 1) * scale, 1 * scale):
        if y == round(eval(function), 0):
            print(end='o')
        elif y == 0 and x != 0:  # x-axis
            print(end='-')
        elif y != 0 and x == 0:  # y-axis
            print(end='|')
        elif y == 0 and x == 0:  # origin
            print(end='+')
        else:
            print(end=' ')
    print('')