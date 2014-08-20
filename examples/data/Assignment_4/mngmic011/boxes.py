#question 1
#Micaela Menegaldo

def print_square ():
    print("*"*5)
    for i in range(3):
        print("*"," "*3,"*",sep='')
    print("*"*5)

def print_rectangle (width,height):
    print('*'*int(width))
    for i in range(height-2):
        print("*"," "*(width-2),"*",sep='')
    print('*'*width)

def get_rectangle (width,height):
    figure=""
    top=("*"*int(width))
    figure+=top+"\n"
    for i in range(height-2):
        middle=("*"+" "*(width-2)+"*")
        figure+=middle+"\n"
    figure+=top
    return figure

    
  
    
