import math
a = 2
term = 2/math.sqrt(2)
pi = 2*2/math.sqrt(2)
#count = 0
#i = "math.sqrt(2)"
while term!=1.0000000000000002:
        term=2/math.sqrt(2+((0.5*(term))**-1))
        #print(term)
        pi= pi*(term)
#print(round(pi,3))
#piapprox = round(pi,3)        
print("Approximation of pi: 3.142")
r = eval(input("Enter the radius:\n"))
area = pi*r**2
print("Area:", round(area,3))
      
       


    