#new function to see if game is stuck or not
def check_stuck(grid):
    """return True if there are no adjacent values that are equal; otherwise False"""
    copy = []
    for i in range(4):
        copy.append([])
        for j in range(4):
            copy[i].append(grid[i][j])   
    zero = True
    array = copy
    b = [1,1,1,1]
    c = 1
    array.insert(0,b)
    array.insert(5,b)
    for row in array:
        row.insert(0,c)
        row.insert(5,c)            
    for y in range(len(array)):
        for x in range(len(array)):
            if array[y][x] != 0:
                if array[y][x] == array[y-1][x] or array[y-1][x] == 0:
                    zero = False
                    break
                else:
                    continue
        return zero
        return grid

def push_up (grid):
    """merge grid values upwards"""
    a = grid
    stuck = check_stuck(a)
    while not stuck:
        b = [1,1]
        c = 1
        #create frame to not get range errors
        a.insert(0,b)
        a.insert(5,b)
        for row in a:
            row.insert(0,c)
            row.insert(5,c)
            print(a)
            for y in range(4):
                for x in range(4):
                    print(a[y][x])
                    #if brick with value
                    if (a[y][x] != 0) and (a[y][x] != 1):
                        #if pushed towards brick which is empty
                        if a[y-1][x] == 0:
                            a[y-1][x] = a[y][x]
                        #if pushed towards brick which is equal
                        elif a[y-1][x] == a[y][x]:
                            a[y-1][x] = (a[y][x])*2                 


def push_down (grid):
    """merge grid values downwards"""

def push_left (grid):
    """merge grid values left"""

def push_right (grid):
    """merge grid values right"""  