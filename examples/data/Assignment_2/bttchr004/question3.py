#Program to calculate area of a circle
#christopher betteridge
#question 3

import math
def Pi():
    nextTerm = 0
    calc = 2
    number = 0
    while (nextTerm != 1):
        number = math.sqrt(2+number)
        nextTerm = 2/number
        calc = calc*nextTerm
        
    return calc
roundcalc = round(Pi(),3)
print("Approximation of pi:", roundcalc)
radius = eval(input("Enter the radius: \n"))
area = (Pi()*radius**2)
print("Area:", round(area,3))
    
