#Assignment 4
#Question 1
#Rabia Parker

def print_square():
    print('*'*5)
    for i in range(3):
        print('*', " "*3,'*',sep="")
    print('*'*5)

def print_rectangle(width, height):
    print('*'*width)
    for i in range(height-2):
        print('*',' '*(width-2),'*',sep="")
    print('*'*width)
    
def get_rectangle(width,height):
    get='*'*width+'\n'
    for i in range(height-2):
        get+=('*'+' '*(width-2)+'*'+'\n')
    get+='*'*width
    return get
        
    