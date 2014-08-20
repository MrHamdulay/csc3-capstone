import math

p = 2*  (2/math.sqrt(2)) * (2/math.sqrt(2+math.sqrt(2))) * (2/math.sqrt(2+math.sqrt(2+math.sqrt(2)))) * (2/math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2))))) * (2/math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2)))))) * (2/math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2))))))) * (2/math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2)))))))) * (2/math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2)))))))))


print("Approximation of pi:",round(p,3))
r   =   eval(input("Enter the radius:\n"))
a = p*(r**2)
print("Area:",round(a,3))