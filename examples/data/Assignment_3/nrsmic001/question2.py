j=eval(input("Enter the height of the triangle:\n"))
for i in range(j+1):
    if(i!=0):
        print(" "*(j-i), end="")
        print("*"*((i*2)-1))    

    