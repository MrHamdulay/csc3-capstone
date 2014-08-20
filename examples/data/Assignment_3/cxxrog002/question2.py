def que2():
    y=eval(input("Enter the height of the triangle:\n"))
    space=(y-1)
    for x in range(1,(y)*2,2):
        print(space*" ",x*"*",sep="")
        space-=1
que2()