import math
def PI():
    nextTerm = 0 
    picalc = 2
    number = 0
    while (nextTerm != 1):
        number = math.sqrt(2+number)
        nextTerm = 2/number
        picalc = picalc*nextTerm
        
    return picalc    
    
rpicalc = round(PI(),3)
print('Approximation of pi:', rpicalc)
radius = eval(input("Enter the radius: \n"))
area = (PI()*radius**2)
print('Area:',round(area, 3))

    