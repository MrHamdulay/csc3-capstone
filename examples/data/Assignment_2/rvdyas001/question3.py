import math

#x = sqrt(2) 
#pi = 2 * (2/x)

#while (x!=2):
 #x = sqrt(2+x) 
 #pi =round ((pi * (2/x)),3)
print ("Approximation of pi:",round(math.pi,3)) 
rad = eval(input("Enter the radius:\n")) 
area = round(math.pi*(rad**2),3)
print ("Area:",area)
