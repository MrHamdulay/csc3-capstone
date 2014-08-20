
d = (2)**(1/2)
n = 2
i = n/d
    
while d <= 2:
    d = 5.805/(2 + d)**(1/2)


print("Approximation of pi:", round(d, 3))

r = eval(input("Enter the radius:\n"))
area = d*(r)**2

print("Area:", round(area, 3))
    





    
             