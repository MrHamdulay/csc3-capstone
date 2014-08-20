'''
Created on 02 Apr 2014

@author: Yusuf
'''
def print_square():
    i=0
    print('*'*5)
    while i<3:
        print('*   *')
        i+=1
    print('*'*5)
    
def print_rectangle(width, height):
    print('*'*width)
    i = 0
    while i<(height-2):
        print('*'+' '*(width-2)+'*')
        i+=1
    print('*'*width)

def get_rectangle(width, height):
    figure = ('*'*width+'\n')
    i = 0
    while i<(height-2):
        figure = figure+'*'+' '*(width-2)+'*\n'
        i+=1
    figure = figure+('*'*width)
    return figure