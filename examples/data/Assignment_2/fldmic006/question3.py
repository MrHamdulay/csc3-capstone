pi = 2
root2 = 2
denom = 0
rounded = 0

while(denom != 2):
        denom = (denom + root2)**0.5
        root2 = (root2 + 2)**0.5
        pi = pi*2/denom

rounded = round(pi, 3)

print("Approximation of pi:", rounded)
radius = eval(input("Enter the radius:\n"))

area = pi * radius**2
print("Area:", round(area, 3))