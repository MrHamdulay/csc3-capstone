height=eval(input("Enter the height of the triangle:\n"))
pat=1
for i in range(1,height+1):
    print(" "*(height-i),end="")
    print("*"*pat,end="")
    print(" "*(height-i))
    pat+=2
    