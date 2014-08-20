def triangle(height):
    base = (height*2)
    space = height-1
    for j in range(0,base,2):
        print(" "*space, end= "")
        print("*"*(j+1))
        space-=1
        
    
height = eval(input("Enter the height of the triangle: \n"))        
triangle(height)