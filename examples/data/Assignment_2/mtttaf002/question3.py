import math

nextValue = 2
pi = 0
temp = 0
check = 0
d= math.sqrt(2)

while check != 1:
    nextValue *= 2/d
    temp = math.sqrt(2 + d)
    d = temp
    pi = nextValue
    check = 1* 2/d
print("Approximation of pi:", round(pi, 3))
a = eval(input("Enter the radius:\n"))
area = round(pi, 4) *a*a
print("Area:", round(area, 3))
    