def triangle():
    height=eval(input("Enter the height of the triangle:\n"))
    x=height
    for i in range(0,height):
        x=x-1
        print(" "*x+(1+2*i)*"*")
        
triangle()