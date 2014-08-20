import math
multiply = 2 * (2/(math.sqrt(2)))
test = math.sqrt(2)
proof = 0
pi = 0
while proof != 1:
    test = math.sqrt(2 + test)
    proof = 2/test
    multiply = multiply * proof
pi = round(multiply,3) 
print("Approximation of pi: " +str(pi))
radius = float(input("Enter the radius:\n"))
area = round((multiply *(radius**2)),3)
print("Area: " + str(area))

