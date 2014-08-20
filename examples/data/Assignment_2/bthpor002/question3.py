#The long calculation thing 
 


from math import * 
a = sqrt(2) 
pi = 2 * (2/a)

while a!=2:
    a= sqrt(2+a)
    pi = pi * (2/a) 
print ("Approximation of pi:",round(pi,3))
radius = eval(input("Enter the radius:\n")) 
print ("Area:",round((pi*(radius)**2),3)) 



