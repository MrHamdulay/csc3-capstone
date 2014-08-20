tri=eval(input("Enter the height of the triangle:\n"))
for i in range(1,tri+1,1):
        gap=tri-i
        print(" "*gap,end="")
        print("*"*((i*2)-1))

        