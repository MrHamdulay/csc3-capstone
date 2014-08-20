# Emmalene Naicker

#Printing a 5*5 square
def print_square():
    
    print("*****")
    print('*   *')
    print('*   *')
    print('*   *')
    print('*****')

#Printing a rectangle
def print_rectangle(width,height):
    
    print('*'*width)
    space=width-2
    for i in range(height-2):
        print('*'+' '*space+'*')
    print('*'*width)

def get_rectangle(width,height):
    
    box='*'*width+'\n'
    for i in range(height-2):
        box+='*'
        for i in range(width-2):
            box+=' '
        box+='*\n'
    box+='*'*width

    return box


