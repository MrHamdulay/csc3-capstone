# Program to create an isoceles triangle
# Khwezi Majola
# MJLKHW001
# 20 March 2014
def tri():
    h = eval(input('Enter the height of the triangle:\n'))
    for i in range(h):
        print(' '*(h-i-1) + '*' * (2*i+1))
tri()