#Circle area calculator
#KVRSHA004

pi = 2
n = 2
sqrt2 = 2**0.5
i = 2

while i>1:
    n = n**0.5
    i = 2/n
    n = 2+sqrt2
    sqrt2 = (2+sqrt2)**0.5
    pi = pi*i

print("Approximation of pi:", round(pi, 3))
r = eval(input("Enter the radius: \n"))
print("Area:", round(pi*r*r, 3))