#Pi approximation and area calculation program
#Student Name: TEMA, Thabo Hebert
#Student number: TMXTHA006
#Date: 11 March 2014

import math
denominator = math.sqrt(2)
product = 2
frac = 2/denominator

while (frac > 1):
    product *= frac
    denominator = math.sqrt(2 + denominator)
    frac = 2/denominator
pi = round(product, 3)
    
print("Approximation of pi:", pi)
r = eval(input("Enter the radius:\n"))
area = (product*(r**2))
a = round(area, 3)
print("Area:", a)