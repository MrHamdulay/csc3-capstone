# krwane001

def triangle(height,base=0):
    for i in range(height):
        print(" "*(height-1)+("*"*(base*2+1)))
        return triangle(height-1,base+1)
height=int(input("Enter the height of the triangle:\n"))

triangle(height)