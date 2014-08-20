#Cherise Dube 
#28 March 2014
#Program to print a triangle of a inputted height
height=eval(input("Enter the height of the triangle:\n"))
star=1
space=height-1
for i in range(height):
        print (" "*space,"*"*star," "*space,sep="")
        star+=2
        space=space-1
        
        
        

