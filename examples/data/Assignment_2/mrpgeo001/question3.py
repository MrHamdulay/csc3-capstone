import math

pi = 2 * (2/(math.sqrt(2))) #initial value of pi
denominator = math.sqrt(2)  #initial denominator
#y = math.sqrt(2)
#z = math.sqrt(2)
while denominator < 2:
    denominator2 = denominator + 2  #adds two to denominator
    denominator2 = math.sqrt(denominator2)   #square roots the denominator
    pi = pi * (2/denominator2)      #updates the value of pi
    denominator = denominator2      #changes the initial value of the denominator



print("Approximation of pi:",round(pi,3))
rad = eval(input("Enter the radius:\n"))
area = pi * (rad**2)       #area formula  
print("Area:",round(area,3))

