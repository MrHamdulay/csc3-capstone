#Dumisani Ngwenza
#NGWDUM005
#22/03/14
# A program that draws an isosceles triangle of a given height using the '*' character and an input

height = eval (input("Enter the height of the triangle:\n"))
gap = height-1
par = 1
char = '*'
for i in range (height):
    print (' '*gap, end = "")
    print (par*char)
    par+=2
    gap -=1
