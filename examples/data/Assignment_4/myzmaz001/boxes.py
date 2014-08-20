#02 April 2014        #Mazwi Myeza
#Assignment 4         #Question1

def print_square():
    print(5*"*")
    for i in range(3):
        print("*"+3*" "+"*")
    print(5*"*")     
    
def print_rectangle(width,height):
    print(width*"*")
    for i in range(height-2):
        print("*"+(width-2)*" "+"*")
    print(width*"*")

def get_rectangle(width,height):
    rectangle = ""
    rectangle = width*'*'+'\n'
    for i in range(height-2):
            rectangle += '*'+(width-2)*" "+'*\n' 
    rectangle += width*'*'+'\n'
    return rectangle
    