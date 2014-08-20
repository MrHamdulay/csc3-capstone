import math
s=math.sqrt

pi=2*(2/s(2))*(2/s(2+s(2)))*(2/s(2+s(2+s(2))))*(2/s(2+s(2+s(2+s(2)))))*(2/s(2+s(2+s(2+s(2+s(2))))))*(2/s(2+s(2+s(2+s(2+s(2+s(2)))))))*(2/s(2+s(2+s(2+s(2+s(2+s(2+s(2))))))))*(2/s(2+s(2+s(2+s(2+s(2+s(2+s(2+s(2)))))))))
print("Approximation of pi:", round(pi,3))

r=eval(input("Enter the radius:\n"))
print("Area:",round(pi*r**2,3))