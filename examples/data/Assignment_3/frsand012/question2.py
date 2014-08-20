def triangle():
    x = eval(input("Enter the height of the triangle: \n"))
    
    gap = x-1
    
    for i in range(1,x*2,2):
        print (gap*(" "),i*("*"),gap*(" "),sep="")
        gap -=1


triangle()
