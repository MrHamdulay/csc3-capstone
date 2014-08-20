# Area of Circles
# 11/3/14
# Sofia Palmer

import math

def circles():
    answer = 1
    numerator = 2
    denominator = math.sqrt(2)
    while(denominator < 2):
        if(denominator == math.sqrt(2)):
            answer *= 2
        answer *= numerator / denominator
        denominator = math.sqrt(2 + denominator)
    print("Approximation of pi:", round(answer,3))
    radius = eval(input("Enter the radius: \n"))
    Area = answer * radius**2
    Area = round(Area,3)
    print("Area:", Area)
circles()
    
    
    
        
           
    