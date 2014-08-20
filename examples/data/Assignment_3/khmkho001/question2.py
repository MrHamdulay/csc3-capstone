def triangle():
    height = eval (input("Enter the height of the triangle:\n"))
    for i in range (height):
        print(" "*(height-1-i)+"*"*(i*2+1))

triangle()