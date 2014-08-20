import math
x= 2*2/math.sqrt(2)*2/math.sqrt(2+math.sqrt(2))*2/math.sqrt(2+math.sqrt(2+math.sqrt(2)))*2/math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2))))*2/math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2)))))*2/math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2))))))*2/math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2)))))))*2/math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2))))))))
v=round(x,3)
print("Approximation of pi:",v,)
y = eval(input("Enter the radius:\n"))
c=round(y**2*x,3)
print("Area:",c,)