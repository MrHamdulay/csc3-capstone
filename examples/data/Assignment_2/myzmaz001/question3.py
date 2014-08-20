#11 March 2014   #Assignment2
#Mazwi Myeza     #Question3
import math
denominator = (2)**0.5
term = 2/denominator
approx_pi = 2*term
while term != 1:
    denominator = (2+denominator)**0.5
    term = 2/denominator
    approx_pi *= term
print("Approximation of pi:",round(approx_pi,3))   
radius = eval(input("Enter the radius:\n"))
area = approx_pi*(radius)**2
print("Area:", round(area,3))
