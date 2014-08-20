h = eval(input("Enter the height of the triangle:\n"))
for i in range(1, h+1):
    if(i!=0):
        print(" "*(((h*2-1)-(i*2-1))//2), end="")
    print("*"*(i*2-1))
    
    