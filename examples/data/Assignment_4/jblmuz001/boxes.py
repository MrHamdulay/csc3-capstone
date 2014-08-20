# Function to write a square
# 2 April 2014
# Muzammil Jable

def print_square():
    for i in range(1,6):
        if i==1 or i==5:
            print("*"*5)
        else:
            print("*   *")

def print_rectangle (width, height):
    for i in range(1,height+1):
        if i==1 or i==height:
            print('*'*width)
        else:
            print('*','*',sep=" "*(width-2))
            
def get_rectangle (width, height):
    s = ''
    for i in range(1,height+1):
            
            if i==1 or i==height:
                s = s +'*'*width +'\n'
            else:
                s = s +'*' + (width -2)*' ' +'*'+'\n'
    return s
    
