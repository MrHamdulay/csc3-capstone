# functions to create hollow boxes
# Kristin Kinmont
# 29 March 2014

def print_square():
    print('*'*5)
    print(('*'+" "*3+'*\n')*3,end="")
    print('*'*5)
    
def print_rectangle(width,height):
    print('*'*width)
    print(('*'+" "*(width-2)+'*\n')*(height-2),end="")
    print('*'*width)
    
def get_rectangle(width,height):
    # box is an ever changing string which is being added to as the program runs
    box ='*'*width+'\n' #row 1
    for i in range(height-2):
        box += '*'+" "*(width-2)+'*\n' 
    box +='*'*width #row 2
    return box

#print(get_rectangle(5,6))