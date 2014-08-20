import math

tot=0
deno= math.sqrt(2) # denominator of square root 2
pi= 2 * (2/deno) #total = 2 x 2/root(2)
while deno!=2:
    deno = math.sqrt(2 + deno)
    pi= pi * (2/deno)
    

print("Approximation of pi:", round(pi,3))



rad = eval(input("Enter the radius: \n"))
area = (pi)*(rad)**2
print("Area:",round(area,3))


 
           