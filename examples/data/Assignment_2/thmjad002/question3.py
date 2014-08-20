#assignment 2
#question 3
#Jadon Thomson

import math

def value_pi():
    b = 2
    a = math.sqrt(2)
    pi = b*(2/a)
    while a < 2:
        a = math.sqrt(2 + a)
        pi = pi*(2/a)
        #pi = round(pi,3)
    print("Approximation of pi:",round(pi,3))
    r = eval(input("Enter the radius:\n"))
    A = pi*(r**2)
    A = round(A,3)
    print("Area:",A)
    
def main():
    value_pi()

main()
