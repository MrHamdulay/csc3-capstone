#Tato Moaki MKXTAT001
#Program  to calculate value of PI and calculate area of circle from given radius
#question3 Assignment2
import math
def main():
    denominator = math.sqrt(2)
    count = 1
    totalDenominator = 1
    
    while(denominator != 2):
        totalDenominator *= denominator
        denominator = math.sqrt(2 + denominator)
        count += 1
        
    expTwo = math.pow(2, count)
    PI = (expTwo / totalDenominator)
    approximatePI = round( ( expTwo / totalDenominator), 3 )
    print("Approximation of pi:",approximatePI)
    
    radius = eval(input("Enter the radius:\n"))
    area = round((PI * math.pow(radius, 2)), 3)
    
    print("Area:",area)
    
main()
    
       

    