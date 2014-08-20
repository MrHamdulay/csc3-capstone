import math
x = 0
statement = 2
pi = 1

while(statement > 1):
    pi = pi*statement
    x = math.sqrt(2 + x)
    statement = 2/x
    
print("Approximation of pi: " + str(round(pi, 3)))
#pi = round(pi, 3)
rad = eval(input("Enter the radius:\n"))
area = pi*(rad**2)
print("Area: " + str(round(area, 3)))


'''
Approximation of pi: 3.142
Enter the radius:
2.5
Area: 19.635
'''
