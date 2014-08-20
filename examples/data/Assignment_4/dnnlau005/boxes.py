def print_square(): #prints 5x5 box on screen
    print("*"*5)
    for i in range(3):
        print("*"+" "*3+"*")
    print("*"*5)
        
def print_rectangle(width,height): #prints box with given width and height
    print("*"*width)
    for i in range(height-2):
        print("*"+" "*(width-2)+"*")
    print("*"*width)

def get_rectangle(width,height): #returns a string containing the code for box with given width and height 
    return ("*"*width+"\n")+("*"+" "*(width-2)+"*"+"\n")*(height-2)+("*"*width)    
     
