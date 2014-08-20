def triangle():
    height=eval(input("Enter the height of the triangle:\n"))
    
    for i in range(0,height,1):
        print (" "*(height-(i+1)),end="")
        print("*"*(i+1),end="")
        print("*"*i)
        
triangle()