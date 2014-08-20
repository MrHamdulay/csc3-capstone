#Ikhlaas Phohplonker
#1 April 2014

#prints a 5x5 box on the screen
def print_square():
    print('*' * 5)
    for i in range(3):
        print('*' , " "*3 , '*' , sep="")
    print('*' * 5)  
    
#prints a box on the screen with given width and height
def print_rectangle(width, height):
    print('*'*width)
    gap=" "
    for i in range(height -2):
        print('*' , gap*(width-2) , '*', sep="")
    print('*'*width)
    
#returns a string containing a box with given width and height
def get_rectangle (width, height): 
    mark='*'
    picture=""
    first_line=(mark*width)+"\n"
    last_line=(mark*width)
    gap=" "
    middle=""
    for i in range(height-2):
        line=mark+(gap*(width-2))+mark+"\n"
        middle=middle+line    
    picture=first_line + middle + last_line
    return picture