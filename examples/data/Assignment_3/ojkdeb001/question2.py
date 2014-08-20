def triangle():
    height= eval(input("Enter the height of the triangle: \n"))

    
    for i in range(height):
        
        print(" "*(height-i-1)+ "*"*(i+1)+"*"*i)
        
          
        
triangle()