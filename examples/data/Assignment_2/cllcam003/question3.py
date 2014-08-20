import math

pi_start=2
count_loop=1
y=math.sqrt(2)
btest = False
while btest == False:
    y = math.sqrt(2)
    for denominator in range(1, count_loop):
        y = math.sqrt(y + 2)
    if 2/y == 1:
        btest = True
    count_loop = count_loop + 1
    pi_start = pi_start*2/y

print("Approximation of pi: " + str(round(pi_start,3)))
radius = eval(input("Enter the radius:\n"))
area = pi_start*radius*radius
print("Area: " + str(round(area, 3)))

