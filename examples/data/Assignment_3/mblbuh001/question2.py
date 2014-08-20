# question2.py
# Name: Buhlebezwe
# Student Number: MBLBUH001
# Date: 23 March 2014

x = eval(input("Enter the height of the triangle:\n"))

gap = x
y = 1
for i in range(x):
    print(' '*(gap-1),end='')
    print('*'*y)
    gap-=1
    y+=2