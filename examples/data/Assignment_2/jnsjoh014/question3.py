import math


def calcPi():
    product = 2
    x = math.sqrt(2)
    count = 1
    while (2/x != 1):
        #print("Iteration:",count,"\tProduct:",product)
        product = product*(2/x)        
        x = math.sqrt(2+x)        
        count+=1
    pi = product 
    return pi
    
        
def userInput():
    radius = eval(input("Enter the radius:\n"))
    return radius
    

def main():  
    pi = calcPi()
    print("Approximation of pi:",round(pi,3))
    radius = userInput()
    area = pi*(radius**2)
    print("Area:",round(area,3))

main()
