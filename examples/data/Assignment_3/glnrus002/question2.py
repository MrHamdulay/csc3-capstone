#question 2
#GLNRUS002
height=eval(input("Enter the height of the triangle:"))
space=height
for i in range (height+1):
    if space !=0:
        print(" "*space,end="")
        space-=1
    print("*"*(i*2-1))
    