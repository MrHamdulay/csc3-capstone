def triangle(s):
    height = eval(input("Enter the height of the triangle:\n"))
    space=(height-1)
    for i in range(1,height+1):
        print(space*" ",((2*i)-1)*s,sep="")
        space-=1
triangle("*")