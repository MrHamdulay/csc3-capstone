# This program calculates the area of a circle by using an 
# approximate value of pi = 3.142 rounded off to 3 decimal points.

# Student Name: Simeon Nandjembo

# Student Number: NNDSIM001

# 13 March 2014

srtwo = 2**(1/2)
denom = srtwo
pie = 2

while True:      
    pie = pie * 2/denom
    check = 2/denom
    
    if check == 1:
        break
    else:
        denom = (denom + 2)**0.5
        continue

print("Approximation of pi:",round(pie,3))

radius = eval(input("Enter the radius:\n"))

area = pie * (radius*radius)

print("Area:",round((area),3))

#Sample I/O:

#Approximation of pi: 3.142
#Enter the radius:
#2.5
#Area: 19.635