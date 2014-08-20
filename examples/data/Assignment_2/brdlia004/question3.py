import math

ans = 2.0  
newT = math.sqrt(2) 
    
while 2/newT != 1.0:
    
    ans = ans*(2/newT)
    newT = math.sqrt(2+newT)
    
pi = round(ans,3)

print("Approximation of pi:", pi)
r = eval(input("Enter the radius:\n"))
area = ans*(r**2)
print("Area:", round(area,3))