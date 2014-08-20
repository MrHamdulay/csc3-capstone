#Question 2
#Assignment 3
#Tauriq Dolley


def isos(height):
    
    spacing = height - 1
    for i in range(0,height,1):
        print(' '*spacing,end='') 
        print('*'*(i+1),end='')
        print('*'*(i))
        
        spacing = spacing - 1
        
height = eval(input("Enter the height of the triangle: \n"))
isos(height)
