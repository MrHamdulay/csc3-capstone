#Calculate pi and then the area, aften input of radius

import math

link=math.sqrt(2)
pi=2

while 2/link > 1:
    pi=pi*2/link
    link =math.sqrt(2+link)
    
calpi=round(pi,3)


print("Approximation of pi:", calpi)
radius = eval(input("Enter the radius: \n"))

area = (radius**2)*pi
area = round(area,3)

print("Area:", area)