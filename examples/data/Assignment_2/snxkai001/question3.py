import math

sq = math.sqrt(2)
a=2/sq
pi = 2*a
while a!=1:
        
        sq=math.sqrt(2+sq)
        
        a=2/sq
        
        pi*=a
        
print("Approximation of pi:",round(pi,3))
      
    
x=eval(input("Enter the radius:\n"))

if(x==int,float):
        area=((math.pi)*(x**2))
        
        
print("Area:",round(area,3))        
        
       
    

