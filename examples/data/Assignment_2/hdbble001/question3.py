import math

i=math.sqrt(2)
x=2*(2/i)
k=3
while k>=1.0000001:
    j=round(math.sqrt(2+i),10)
    k=round(2/j,10)
    x*=k
    i=j
    

print("Approximation of pi:" ,round(x,3))
y=eval(input("Enter the radius:\n"))
print("Area:", round(x*(y**2),3))
