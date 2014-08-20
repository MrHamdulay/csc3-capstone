# Author Richard Marais
def print_rectangle(width,height):

    j=0                               
    k=height
    for i in range(height):                 
        if j<1 or j>(height-2):          #configuring the empty space area in the rectangle
            print(width*'*')
        
        else:
            print('*',(width-2)*' ','*',sep='')
        j=j+1   



def print_square():
    j=0
    k=5
    for i in range(5):
        if j<1 or j>(5-2):
            print(5*'*')
        
        else:
            print('*',(5-2)*' ','*',sep='')
        j=j+1   


def get_rectangle(width,height):
    output = ""
    j=0
    k=height
    for i in range(height):
        if j<1 or j>(height-2):
            output+=(width*'*')+"\n"
        
        else:
            output+=('*' + (width-2)*' ' + '*')+"\n"
        j=j+1
    return output