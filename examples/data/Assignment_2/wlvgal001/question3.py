#Galya Wolov
#Area of Circle Calculator
#9/03
import math
currentterm=math.sqrt(2)

newterm=2
accu=2

while newterm != 1:    
    newterm= 2/currentterm
    accu *= newterm
    currentterm= math.sqrt(2+currentterm)

accumu=round(accu,3)

print("Approximation of pi:", accumu)
radius= eval(input("Enter the radius:\n"))
print("Area:",round((radius*radius)*accu,3))


