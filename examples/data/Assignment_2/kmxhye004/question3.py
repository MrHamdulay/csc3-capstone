pi = 2
denominator = 0

while(denominator<2):
    denominator = (2+denominator)**0.5
    pi= pi*2/denominator


print("Approximation of pi:", round(pi,3))    
radius=eval(input("Enter the radius: \n"))               
area=round(pi*(radius*radius),3)
print("Area:",str(area))
