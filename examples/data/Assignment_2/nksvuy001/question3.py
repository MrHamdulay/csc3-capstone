#program that calculates the value of PI
#vuyolwethu nkosi
#10 march 2014

from math import*
m=sqrt(2)
n_pi=2*(2/m)

while(m!=2):
    m=sqrt(2+m)
    n_pi=n_pi*(2/m)

print("Approximation of pi:",round(n_pi,3))
o_r=eval(input("Enter the radius:\n"))
print("Area:",round((n_pi*o_r**2),3))
    
    
    
    
    
    
    
    
