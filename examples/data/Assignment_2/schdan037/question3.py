#Assignment 2, question 3
#Determines leap year
#Daniel Schwartz
#SCHDAN037
#09/03/2014

import math

def get_pi():
    x = math.sqrt(2 + math.sqrt(2))
    pi = 2 * 2/math.sqrt(2)
    while(2/x != 1):
        pi *= 2/(x)
        x = math.sqrt(2+x)
    return pi

def find_area(r):
    
    area = get_pi() * r**2
    print ("Area:", round(area, 3))

if __name__ == '__main__':
    print("Approximation of pi:", round(get_pi(), 3), end="\n")
    find_area(eval(input("Enter the radius:\n")))
