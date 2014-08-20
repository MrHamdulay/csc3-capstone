import math

def calcPi():
    sq2 = math.sqrt(2)
    pi = 2*2/sq2
    while(2/sq2!=1):
        sq2 = math.sqrt(2+sq2)
        pi = pi*2/sq2        
    return(pi)   
        
print("Approximation of pi:",round(calcPi(),3))
radius = eval(input("Enter the radius:\n"))
print("Area:",round(calcPi()*radius**2,3))
        
    
