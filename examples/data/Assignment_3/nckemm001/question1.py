# Question 1



height=eval(input("Enter the height of the rectangle:\n"))
width=eval(input("Enter the width of the rectangle:\n"))

def rec(height,width):

    for i in range(height):
        print("*"*width)

rec(height,width)