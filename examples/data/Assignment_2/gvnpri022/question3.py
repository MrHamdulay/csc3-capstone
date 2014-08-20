import math
term = 0
x=0
pi=2
den=0;
while(term!=1):
  
    den=math.sqrt(den+2)
        #print(den)
    

    term=2/den
    #print(term)
    pi=pi*term
    x=x+1
#print(pi)
print("Approximation of pi:",round(pi,3))
rad= eval(input("Enter the radius:\n"))
area= pi*(rad**2)
print("Area:", round(area,3))
          