h=eval(input("Enter the height of the triangle: \n"))
y=" "
z=1
while h>=1:
    print(y*(h-1),z*"*", sep="")
    z+=2
    h=h-1