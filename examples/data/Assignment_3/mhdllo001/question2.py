height=eval(input("Enter the height of the triangle:\n"))
t=1
for i in range(1, height+1):
    print(" "*(height-i)+"*"*t)
    t+=2
