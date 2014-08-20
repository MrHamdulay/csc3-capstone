height=eval(input("Enter the height of the triangle:\n"))

for i in range(1,height+1,1):
    print(" "*(height-i)+"*"*(2*i-1))