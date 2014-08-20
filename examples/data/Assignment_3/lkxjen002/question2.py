def tri():
    height=eval(input("Enter the height of the triangle:\n"))
    gap=height
    count=1
    for i in range(height):
        gap-=1
        print(gap*" ", end="")
        print("*"*count)
        count+=2
tri()