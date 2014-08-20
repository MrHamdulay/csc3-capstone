# Yentl Naidu (NDXYEN001)
# Assignment 3
# 26 March 2014
# Question 2

def triangle(h):
    for i in range(h):
        print((' ' * ( h - i - 1 ) + '*' * ( 2 * i + 1)))

h = eval(input("Enter the height of the triangle:\n"))

triangle(h)
