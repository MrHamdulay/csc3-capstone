import math

x=2*(2/math.sqrt(2))*(2/(math.sqrt(2+math.sqrt(2))))*(2/(math.sqrt(2+math.sqrt(2+math.sqrt(2)))))*(2/(math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2))))))*(2/(math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2)))))))*(2/(math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2))))))))*(2/(math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2)))))))))
y=round(x,3)

print("Approximation of pi:",y)
z=eval(input("Enter the radius:\n"))
a=math.pi*z**2
print("Area:",round(a,3))
