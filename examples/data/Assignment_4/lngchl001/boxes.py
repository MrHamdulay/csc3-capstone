def print_square():
    print("*"*5)
    print("*"," "*1,"*")
    print("*"," "*1,"*")   
    print("*"," "*1,"*")
    print("*"*5)
def print_rectangle(width,height):
    print("*"*width)
    for i in range(height-2):
        print("*",end='')
        print(' '*(width-2),end='')
        print("*")
    print("*"*width) 
    
def get_rectangle(width,height):
    rec=''
    rec=rec+"*"*width
    for i in range(height-2):
        rec=rec+'\n'+'*'
        rec=rec+' '*(width-2)
        rec=rec+'*'
    rec=rec+'\n'+"*"*width
    return rec  
       