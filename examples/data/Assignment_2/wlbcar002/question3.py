import math
#print(2*(2/math.sqrt(2))*(2/math.sqrt(2+math.sqrt(2)))*(2/math.sqrt(2+math.sqrt(2+math.sqrt(2)))))
pi = 0
#i = math.sqrt(2)
#k = 0
#while i >1:
    #k = 2/math.sqrt(i)
    #print(i)
    #print(k)
    #k+1
    
a= 2
k = math.sqrt(2)
for i in range(100):
    k = math.sqrt(2+k)
    a *=2/k
    #print(k)
    #print(a)
    
    
#for i in range(10):
pi = a*2/math.sqrt(2)
#print(pi)

print("Approximation of pi:",round(pi,3))
rad = eval(input("Enter the radius:\n"))
area = pi*(rad**2)
print("Area:",round(area,3))
