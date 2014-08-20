height=eval(input("Enter the height of the triangle:\n"))
x=1
space=height-1
for i in range(height):
    print(" "*space,"*"*x, sep="")
    x=x+2
    space=space-1

    
    
    
    