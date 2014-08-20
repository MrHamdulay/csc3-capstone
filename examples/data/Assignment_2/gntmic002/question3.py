import math

pi = 2
count = 1
y = math.sqrt(2)
bTest = False
while bTest == False:
    y = math.sqrt(2)
    for k in range(1, count):
        y = math.sqrt(y + 2)
    if 2/y == 1:
        bTest = True
    count = count + 1
    pi = pi*2/y

print("Approximation of pi: " + str(round(pi,3)))
radius = eval(input("Enter the radius:\n"))
area = pi*radius*radius
print("Area: " + str(round(area, 3)))
    
    

        