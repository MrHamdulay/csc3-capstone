import math
#pi = 2*(2/math.sqrt(2))*(2/math.sqrt(2+math.sqrt(2)))*(2/math.sqrt(2+math.sqrt(2+math.sqrt(2))))*(2/math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2)))))*(2/math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2))))))
pi=1
denom = 0
term = 2
while (term != 1):
    pi*=term
    term = 2/math.sqrt(2+denom)
    denom = math.sqrt(2+denom)
print("Approximation of pi:",round(pi,3))
radius = eval(input("Enter the radius:\n"))
print("Area:",round((pi*radius*radius),3))

