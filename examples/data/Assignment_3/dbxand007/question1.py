#Cherise Dube
#28 March 2014
#Program to print a rectangle of given height and width 
def rectangle():
    height= eval(input("Enter the height of the rectangle:\n"))
    width=eval(input("Enter the width of the rectangle:\n"))
    for i in range(height):
        print(width*"*")
rectangle()
