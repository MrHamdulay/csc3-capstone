height=eval(input("Enter the height of the triangle:\n"))
x=height
gaps=x-1
for i in range(2,2*x+1,2):    
    print(" "*gaps,"*"*(i-1), sep="")
    gaps=gaps-1