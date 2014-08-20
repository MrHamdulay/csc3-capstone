#formula for triangle rows=2n-1
def tri():
    height=eval(input("Enter the height of the triangle:\n"))
    gap=height-1
    for i in range(1,height+1):
        print(" "*gap,end="")
        print("*"*(2*i-1))
        gap=gap-1   
tri()
        
        