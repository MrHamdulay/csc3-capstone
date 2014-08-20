pi=2
denom=0
while(denom<2):
    denom=(2+denom)**0.5
    pi=pi*2/denom
    
print("Approximation of pi:", round(pi,3))
radius=eval(input("Enter the radius:\n"))
area=round(pi*(radius*radius),3)
print("Area:",str(area))
