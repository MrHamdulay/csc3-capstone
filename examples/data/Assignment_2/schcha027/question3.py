import math
stop=0

#while not stop==1:
a=2
pi=0
k=math.sqrt(2)

for i in range(100):
    #pi=2/(k)
    k= math.sqrt(2+k)
    a=a*2/k
    
b=a*2/math.sqrt(2)
c=round(b,3)
print("Approximation of pi:",c)
userData=eval(input("Enter the radius:\n"))
area=(b*(userData**2))
print("Area:",round(area,3))
