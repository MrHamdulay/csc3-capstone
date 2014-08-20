# A program to create hollow boxes of stars
# Alison Hoernle
# HRNALI002
# 28 March 2014

def print_square():
    print('*'*5)
    for i in range(1,4):
        print('*   *')
    print('*'*5)

def print_rectangle(width, height):
    #first line of stars
    print('*'*width)
    
    #next lines with hollow space
    for i in range(height - 2):
        print('*', ' '*(width - 2), '*', sep = '')
    
    #bottom line of stars
    print('*'*width)

def get_rectangle(width, height):
    z = width - 2
    
    # for 1st and last line
    x = '*'*width
    
    #start with this result and add from there
    result = str(x) #Must make a string
    
    #Loop for the hollow part of rectangle
    for i in range(1, height-1):
        pattern = '*' + ' '*z + '*'
        pattern_new = str(pattern) #must make a string
        result = result + '\n' + pattern_new # strings do not use commas to separate the parts, but rather use + like concatenation.
    result = result + '\n' + x
    
    return result #NB can only return once in a function