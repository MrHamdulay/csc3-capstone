#Program to print a rectangular box
#Program to print a triangle
#Written By: Suvir Gajadhur



height = eval(input("Enter the height of the triangle:\n"))
y = height*2 - 1
gap = y//2

for i in range(0,y,2):
    print(' '*gap,end='')
    print("*"*(i+1))
    gap = gap-1
    
    
    
    