x = eval(input("Enter the height of the triangle:\n"))
star = 1
for i in range(1,(x+1)):
    print(" "*(x-i),"*"*(star), " "*(x-i), sep="")
    star+=2