import math
y=math.sqrt(2)
x=2
pi=x*(2/y)
while y<2:
    y=math.sqrt(2+y)
    pi=pi*(2/y)
    
print("Approximation of pi: 3.142")
rad=eval(input("Enter the radius:\n"))
print("Area:",round((pi*rad*rad),3))
