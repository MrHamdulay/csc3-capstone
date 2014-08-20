# Luke Henkeman, HNKLUK001
# CSC1015F, Assignment 4, Q1
# 30 March 2014

def print_square():
    print('*'*5)
    for i in range(3):
        print('*',' ','*')
        i+=1
    print('*'*5)

def print_rectangle(width, height):
    print('*'*width)
    for i in range(height-2):
        print('*',(width-2)*' ','*',sep='')
        i+=1
    print('*'*width)
    
def get_rectangle(width, height):
    result = '*'*width+"\n"
    for i in range(height-2):
        result += '*'+(width-2)*' '+"*\n"
        i+=1
    result += '*'*width
    return result 
    