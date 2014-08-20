import math

def approximate_pi():
    denominator = 0
    output = 2
    i = 0
    while True:
        denominator = math.sqrt(2 + denominator)
        term = 2/denominator
        output *= term
        if (term == 1):
            break
    return output
        
pi = approximate_pi()

print("Approximation of pi:", round(pi,3))
radius = float(input("Enter the radius:\n"))
area = pi * radius * radius
print("Area:", round(area, 3))