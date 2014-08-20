import math
pi=2
divisor=math.sqrt(2)
while (2/divisor)!=1:
    pi*=2/divisor
    divisor=math.sqrt(2+divisor)
print("Approximation of pi:", round(pi, 3))
radius=eval(input("Enter the radius: "))
area = pi*(radius**2) 

print("\nArea:", round(area, 3))


    

    
    

    
        
    
    
    
    