#Mbongeni Mazibuko
#MZBMO002
#Assignment 4

def print_square():
    for i in range(1,6):
        if i==1 or i==5:
            print('*'*5)
        else: print('*',' '*3,'*',sep='')
        
def print_rectangle(width, height):
    for i in range(1,height+1):
        if i==1 or i==height:
            print('*'*width)
        else: print('*',' '*(width-2),'*',sep='')
        
def get_rectangle(width, height):
    rect=''
    for i in range(1,height+1):
        if i==1 or i==height:
            rect+= '*'*width +'\n'
        else: rect+= '*'+' '*(width-2)+'*' + '\n'
    return rect