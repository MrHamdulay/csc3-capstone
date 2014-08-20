height=eval(input("Enter the height of the rectangle:\n"))
width=eval(input("Enter the width of the rectangle:\n"))    
char="*"

def rect(height,width):
    for i in range(height):
        print(char*width)
        
rect(height,width)