def isoceles(height):
    gap=height-1
    star=1
    for i in range(height):
        print(gap*" ", end="")
        print(star*"*")
        gap-=1
        star+=2
height=eval(input("Enter the height of the triangle:\n"))
isoceles(height)
    