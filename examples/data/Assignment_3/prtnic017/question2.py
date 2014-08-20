# Student Number: PRTNIC017
# Date: 3/16/14

height = eval(input('Enter the height of the triangle:\n'))
h = height * 2
for x in range(1, h, 2):
    sep = ' ' * ((h - x) // 2)
    print(sep, '*' * x, sep='')