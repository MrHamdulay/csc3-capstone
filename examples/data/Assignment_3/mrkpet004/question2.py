height=eval(input("Enter the height of the triangle:\n"))
char="*"

def isoc(height):
    gap=height-1
    for i in range(0,height*2,2):
        print(" "*gap,end="")
        print(char*(i+1))
        gap-=1
        
isoc(height)
    