h=eval(input("Enter the height of the triangle:\n")) 

def triangle(h,b):
    gap=(h//2)-1
    for i in range (0,h,2):
        print(" "*gap,end="")
        print(b*(i+1))
        gap-=1
       
triangle(h*2,"*")