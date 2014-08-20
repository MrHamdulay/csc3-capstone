# Approximation of pi and raidus calculation
temp = 0
pi = 2
for i in range(20):
    for j in range(i):
        temp = (2+temp)**(1/2)
        pi *= 2/temp
print("Approximation of pi:",round(pi,3))
rad = eval(input("Enter the radius:\n"))
area = round(pi*rad*rad,3)
print("Area:",area)