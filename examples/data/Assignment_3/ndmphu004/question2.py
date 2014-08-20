y=eval(input("Enter the height of the triangle:\n"))
star=1
for i in range(0,y,1):
    print((y-i-1)*" "+star*("*"))