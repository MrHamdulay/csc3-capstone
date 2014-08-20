def print_square ():
    print('*'*5)
    print('*','   ','*',sep='')
    print('*','   ','*',sep='')
    print('*','   ','*',sep='')
    print('*'*5)
    
def print_rectangle (width,height):
    print('*'*width)
    for i in range(height-2):
        print('*',' '*(width-2),'*',sep='')
    print('*'*width)

def get_rectangle(width,height):
    output = "*" * width + "\n" 
    for i in range(height-2):
        output+= ( "*" + " " * (width-2) + "*" + "\n")
    output+= "*" * width
    return output
    