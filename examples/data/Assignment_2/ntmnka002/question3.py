import math

Sum = math.sqrt(2)
Answer = 2

#While loop
while (2/Sum != 1):
    Answer = Answer * (2 / Sum)
    Sum = math.sqrt(2 + Sum)
    
print('Approximation of pi:', round(Answer, 3)) 
Radius = eval(input('Enter the radius:\n'))

Area = Answer * Radius**2 

print('Area:', round(Area, 3))