height=eval(input("Enter the height of the triangle:\n"))
stars=1
gap=((2*height)-1)//2

for i in range(1, height+1):
    print(" "*gap, end="")
    print("*"*stars)
    gap-=1
    stars+=2