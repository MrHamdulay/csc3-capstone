


import math
pi = 2
den = math.sqrt(2)
while 2/den >1:
    pi = pi*2/den
    den = math.sqrt(2+den)
    
a = round(pi,3)

print("Approximation of pi:",a)
rad = eval(input("Enter the radius:\n"))
A = pi*rad**2
print("Area:",round(A,3))


               
               


    
    
    
    
    

