H=eval(input("Enter the height of the triangle:\n"))
B=2*H-1
gap=B//2
for i in range(0,B,2):
        print(" "*gap,end="")
        print("*"*(i+1))
        gap-=1
        
    



