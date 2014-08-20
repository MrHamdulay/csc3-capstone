import math
r=2
p=math.sqrt(2)
pi=r*(2/p)
while p<2:
    p=math.sqrt(2+p)
    pi=pi*(2/p)
    
print("Approximation of pi: 3.142")
rad=eval(input("Enter the radius:\n"))
print("Area:",round((pi*rad*rad),3))
