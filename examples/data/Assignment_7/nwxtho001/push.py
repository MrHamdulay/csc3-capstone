'''
a module to push things with great gusto
tom new
2014/04/28
'''

def mirror (grid):
    '''Takes the mirror image of a 4x4 grid along the top-left-bottom-right diagonal'''
    for row in range (1, 4):
        for col in range (3):
            if row == col:
                break
            else:
                grid [row][col], grid [col][row] = grid [col][row], grid [row][col]

def squash (x):
    '''Removes all zeroes from a list'''
    while 0 in x:
        x.remove (0)
    
def merge (x):
    '''Merges like values in a list from left to right'''
    if len (x) < 2:
        return x
    elif x [0] == x [1]:
        return [x [0] * 2] + merge (x [2:])
    else:
        return [x [0]] + merge (x [1:])

def fill (x):
    '''Appends zeroes to a list until it contains 4 items'''
    while len (x) < 4:
        x.append (0)
        
def push_left (grid):
    '''Merges grid values left'''
    for row in range (4):
        squash (grid [row])
        grid [row] = merge (grid [row])
        fill (grid [row])

def push_right (grid):
    '''Merges grid values right'''
    for row in range (4):
        grid [row].reverse ( )
        squash (grid [row])
        grid [row] = merge (grid [row])
        fill (grid [row])
        grid [row].reverse ( )

def push_up (grid):
    '''Merges grid values upwards'''
    mirror (grid)
    push_left (grid)
    mirror (grid)
    
def push_down (grid):
    '''Merges grid values downwards'''
    mirror (grid)
    push_right (grid)
    mirror (grid)    