def print_square():
    for i in range(1,6):
        if i == 1 or i == 5:
            print("*"*5)
        else: 
            print("*"," "*3,"*",sep='')
    
def get_rectangle(width,height):
    returnstring = "*"*width+"\n"
    for i in range(1,height):
        if i == height-1:
            returnstring += "*"*width
        else:
            returnstring += "*"+" "*(width-2)+"*"+"\n"
    return returnstring

def print_rectangle(width,height):
    print(get_rectangle(width,height))
            