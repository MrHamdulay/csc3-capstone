#Using if, for and while loops to make shapes
#Kenneth Shimabukuro
#19/03/14
height = eval(input("Enter the height of the rectangle:\n"))
width = eval(input("Enter the width of the rectangle:\n"))   

def sq():
   for i in range(0,height,1):
       print("*"*width)
sq()       