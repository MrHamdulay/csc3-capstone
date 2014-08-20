'''Another utility program, last one got corrupt
I hate windows 8 right now
Ednecia Matlapeng
'''
def create_grid(grid):
    """create a 4x4 grid"""
    for i in range(0,4):
        grid.append([0]*4)
    return grid
        

def print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    output = '+'+'-'*20+'+\n'
    for line in grid:
        output+='|'
        for value in line:
            if value == 0:
                output += ' '*5
            else:
                output += str(value)+' '*(5-len(str(value)))
        output+='|\n'
    output += '+'+'-'*20+'+'
    print( output)
        

def check_lost (grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    check = True
    for i in range(0,4):
        for k in range(0,4):
            if grid[i][k]==0:
                check = False
                break
    if check == True:
        #Check for the adjacent values: left vertices 
        if grid[0][0]== grid[0][1] or grid[0][0]== grid[1][0] :
            check = False
        elif grid[3][0]== grid[3][1] or grid[3][0]== grid[2][1] :
            check = False
        #Check for the adjacent values :right vertices
        elif grid[3][3]== grid[3][2] or grid[3][3]== grid[2][3] :
            check = False  
        elif grid[0][3]== grid[1][3] or grid[0][3]== grid[0][2] :
            check = False         
    #Trying something different for the edges
        else: 
            for i in range(0,4):
                for k in range(0,4):
                   
                   #The left edge
                    if k==0:
                        if grid[i][k]==grid[i][k+1]:
                            check =False
                 #The right edge
                    elif k==3:
                        if grid[i][k]==grid[i][k-1]:
                            check =False                    
                    #The bottom edge
                    elif i==3:
                        if grid[i][k]==grid[i-1][k]:
                            check =False  
                    #The top edge
                    else:
                        if grid[i][k]==grid[i+1][k]:
                            check =False  
    return check

def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    check = False
    for i in grid:
        for value in i:
            if value>=32:
                check = True
                break
    return check
    

def copy_grid (grid):
    """return a copy of the grid"""
    gridcopy = []
    for i in grid:
        temp = []
        for k in i:
            temp.append(k)
        gridcopy.append(temp)
    return gridcopy
        

def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    check = True
    for i in range(0,4):
        for k in range(0,4):
            if grid1[i][k]!=grid2[i][k]:
                check = False
                break
    return check
#I did all my checking here
grid =[[44, 45, 40, 43], [1, 11, 12, 13], [2, 22, 23, 24], [31, 900, 32, 33]]
##grid=(create_grid(grid))
#print(check_lost(grid))
#print(print_grid (grid))
lack =(copy_grid(grid))
#print(lack)
#print(grid_equal (grid, lack))