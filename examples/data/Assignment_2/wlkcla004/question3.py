import math

x=2
i=math.sqrt(2)
li=2


while True:
    import math
    n = x/i
    if n == 1:
        print("Approximation of pi:", round(li,3))
        r=eval(input("Enter the radius:\n"))
        print("Area:", round(li*r**2,3))      
        break
    else:
        li=li*n
        i=math.sqrt(2+i)
       
 
       
    