#a program that generates a triangle
#23/03/2014
#kk mphele

def triangle():
    height=eval(input("Enter the height of the triangle:\n"))
    
    height*=2
    gap=height//2-1
    for i in range(0,height,2):
        print(" "*gap,end="")
        i+=1
        print("*"*(i))
        gap=gap-1
        
triangle()