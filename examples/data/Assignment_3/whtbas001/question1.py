#WHTBAS001
#ASSIGNMENT 3
#QUESTION 1
#25-03-2014

def rectangle(a,b):
    for i in range(a):
        print("*"*b, end="\n")

height = int(eval(input("Enter the height of the rectangle: \n")))
width = int(eval(input("Enter the width of the rectangle: \n")))

rectangle(height, width)

#Done