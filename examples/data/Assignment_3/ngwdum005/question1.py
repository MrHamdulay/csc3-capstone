#Dumisani Ngwenza
#NGWDUM005
#22/03/2014
#A program that draws a rectangle of a given height and width using the '*' character.

height = eval (input ("Enter the height of the rectangle:\n"))
width = eval (input ("Enter the width of the rectangle:\n"))
char = '*'

for i in range(height):
    print (char*width)
    
