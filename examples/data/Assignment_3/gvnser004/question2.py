h=eval(input("Enter the height of the triangle:\n"))

for i in range(h):
    
    print(" "*(h-(i+1)),end="")
    
    print("*"*(i+1),end="")
    print("*"*(i),end="")
    
    
    print()