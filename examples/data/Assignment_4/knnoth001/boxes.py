# Module that contains functions that print or return a box 
# Name: Othniel KONAN
# Student number: KNNOTH001
# Date: 2014/03/29

def print_square ():
    
    nb=5
    print('*'*nb)
    for i in range(nb-2):
        print('*',' '*(nb-2),'*',sep='')
    print('*'*nb)
    

def print_rectangle (width, height):
    
    print('*'*width)
    for i in range(height-2):
        print('*',' '*(width-2),'*',sep='')
    print('*'*width)    
    
def get_rectangle (width, height):
    pic = '*'*width+'\n'
    for i in range(height-2):
        pic += '*'+' '*(width-2)+'*'+'\n'
    pic += '*'*width
    return pic
        