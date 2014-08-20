height=eval(input("Enter the height of the triangle:\n"))
def triangle(height):
    gap=(height-1)
    for i in range(0,height*2-1,2):
        print(" "*gap,end="")
        print("*"*(1+i))
        gap-=1
        
triangle(height)