def print_square():
    for i in range(1,6):
        if i ==1 or i==5:
            print('*'*5)
        else:
            print('*'+' '*3+'*')
def print_rectangle(width, height):
    for i in range(1,height+1):
        if i==1 or i ==height:
            print('*'*width)
        else:
            print('*'+' '*(width-2)+'*')

def get_rectangle(width, height):
    out=""
    for i in range(1,height+1):
            if i==1 or i ==height:
                out+='*'*width+"\n"
            else:
                out+='*'+' '*(width-2)+'*'+"\n"
    return out


    
