#calculating the area 
#Siphesihle Cele
#17 march 2014

import math   #math function imported

comp1=math.sqrt(2)       #looped equation being given a variable
approx_pi=2*(2/comp1)

while comp1!=2:               #while loop to repeat the equation given it does not equal 2
    comp1= math.sqrt(comp1+2)
    approx_pi=approx_pi*(2/comp1)        #Approximating Pi value
round_pi=round(approx_pi,3)
print("Approximation of pi:",round_pi)  #Print out of the pi value
radius=eval(input("Enter the radius:\n"))

area_circle= round_pi*radius**2   #area calculated

round_area= round(area_circle,3)
print("Area:",round_area)     #printing the area out.