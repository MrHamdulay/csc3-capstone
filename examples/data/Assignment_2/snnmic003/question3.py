import math

def main():
    prod = 2.0
    i = math.sqrt(2)
    j = 2
    
    while (2/math.sqrt(j) != 1):
        prod = prod * (2 / (math.sqrt(j)))
        j = 2+i
        i = math.sqrt(j)
        
    print ("Approximation of pi:" , round (prod, 3))
    
    radius = eval (input ("Enter the radius:\n"))
    Area = prod * (radius**2) 
    print ("Area:" , round (Area,3))

main()