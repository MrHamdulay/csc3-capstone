import math

s = math.sqrt(2)
a=2
n=2
i=2

while i>1:
    n=math.sqrt(n)
    i=2/n
    n=2+s
    s=(math.sqrt(2+s))
    a=a*i
    
b=round(a,3)
    
print("Approximation of pi:", b)
rad=eval(input("Enter the radius:\n"))
area = round((a*rad*rad),3)
print("Area:", area)
        