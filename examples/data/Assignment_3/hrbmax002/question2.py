height = eval(input("Enter the height of the triangle:\n"))
power = 1

for i in range (0,height):
    print(" "*(height-1), "*"*power, sep="")
    height-=1
    power+=2


