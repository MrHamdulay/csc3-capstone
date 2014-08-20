#assignment3 questiion2
#isosceles triangle
#Smanga

height = eval(input("Enter the height of the triangle:\n"))


def triangle(height):
    space= height-1
    for i in range(1,(2*height),2):
        print(" "*space, end="")
        print('*'*(i))
        space-=1
        
triangle(height)