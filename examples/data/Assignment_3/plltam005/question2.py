def isoc():
    x=eval(input("Enter the height of the triangle:\n"))
    for i in range(x):
        l=((i+1)*2)-1
        k=(x-1)-i
        print(k*" ",l*"*",sep="")
    
isoc()
