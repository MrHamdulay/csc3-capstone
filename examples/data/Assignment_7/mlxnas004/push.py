"""nasha somoina meoli
1st may 2014
program to merge cells to the left, right, up and down"""
def push_left (grid):
    """merge grid values left"""
    
    # create a grid with the elements of the row
    grid2 = []
    for row in range(4):
        pushgrid = []
       
        for col in range(4):
            pushgrid.append(grid[row][col])
        #take the place of zeroes
        while 0 in pushgrid:
            pushgrid.remove(0)
            # merge cells of equal value
        for i in range(len(pushgrid)-1):
            if pushgrid[i] == pushgrid[i+1]:
                pushgrid[i] += pushgrid[i+1]
                pushgrid[i+1] = 0
        #remove zeroes
        while 0 in pushgrid:
            pushgrid.remove(0)        
        # fill up the grid to length of 4
        while len(pushgrid) < 4:
            pushgrid.append(0)
        
        #add all the pushgrids to grid2
        grid2.append(pushgrid)
    for col in range(4):
        for row in range(4):
            grid[row][col] = grid2[row][col]
    return (grid)
def push_right (grid):
    """merge grid values right"""
    # create a grid with the elements of the row
    grid2 = []
    for row in range(4):
        pushgrid = []
       
        for col in range(4):
            pushgrid.append(grid[row][col])
        #take the place of zeroes
        while 0 in pushgrid:
            pushgrid.remove(0)
            # merge cells of equal value
        for i in range(len(pushgrid)-1):
            if pushgrid[i] == pushgrid[i+1]:
                pushgrid[i] += pushgrid[i+1]
                pushgrid[i+1] = 0
        while 0 in pushgrid:
            pushgrid.remove(0)        
        # fill up the grid to length of 4
        while len(pushgrid) < 4:
            pushgrid.insert(0,0)
            
            #add all the pushgrids to grid2
        grid2.append(pushgrid)
    for col in range(4):
        for row in range(4):
            grid[row][col] = grid2[row][col]
    return (grid)    
    
    
def push_up (grid):
           
    """merge grid values left"""

    # create a grid with the elements of the row
    grid2 = []
    for col in range(4):
        pushgrid = []
       
        for row in range(4):
            pushgrid.append(grid[row][col])
        
        #take the place of zeroes
        while 0 in pushgrid:
            pushgrid.remove(0)
            # merge cells of equal value
        for i in range(len(pushgrid)-1):
            if pushgrid[i] == pushgrid[i+1]:
                pushgrid[i] += pushgrid[i+1]
                pushgrid[i+1] = 0
        while 0 in pushgrid:
            pushgrid.remove(0)        
        # fill up the grid to lenth of 4
        while len(pushgrid) < 4:
            pushgrid.append(0)
        
        #add all the pushgrids to grid2
        grid2.append(pushgrid)
    grid5 = []
    for row in range(4):
        grid4 = []
        for col in range(4):
            grid4.append(grid2[col][row])
        grid5.append(grid4)
    for col in range(4):
                for row in range(4):
                    grid[row][col] = grid5[row][col]     
    return (grid)


def push_down(grid):
    
    """merge grid values left"""

    # create a grid with the elements of the row
    grid2 = []
    for col in range(4):
        pushgrid = []
       
        for row in range(4):
            pushgrid.append(grid[row][col])

        #take the place of zeroes
        while 0 in pushgrid:
            pushgrid.remove(0)
            # merge cells of equal value
        for i in range(len(pushgrid)-1):
            if pushgrid[i] == pushgrid[i+1]:
                pushgrid[i] += pushgrid[i+1]
                pushgrid[i+1] = 0
        while 0 in pushgrid:
            pushgrid.remove(0)                
        # fill up the grid to lenth of 4
        while len(pushgrid) < 4:
            pushgrid.insert(0,0)
        
        #add all the pushgrids to grid2
        grid2.append(pushgrid)
    grid5 = []
    for row in range(4):
        grid4 = []
        for col in range(4):
            grid4.append(grid2[col][row])
        grid5.append(grid4)
    
    for col in range(4):
                for row in range(4):
                    grid[row][col] = grid5[row][col]     
    return (grid)
    