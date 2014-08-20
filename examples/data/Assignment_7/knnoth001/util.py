'''Module util for 2048 game
Othniel KONAN
KNNOTH001
2014/04/27'''

#CREATION OF THE GRID 
def create_grid(grid):
    """create a 4x4 grid"""
    for i in range(4):
        grid.append([0]*4)
    return grid

#PRINT THE GRID
def print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    print('+','-'*20,'+',sep='')                                    #print the top frame
    for y in range(4):
        print('|',end='')                                           #start each line with '|'
        for x in range(4):
            if grid[y][x] == 0:                                     #change the value of the grid if its value is 0
                print('{0:<5}'.format(''),end='')
            else:
                print('{0:<5}'.format(grid[y][x]),end='')               #print the value in the right format
        print('|')                                                  #close each line with '|'
    print('+','-'*20,'+',sep='')                                    #print the bottom frame

#CHECK IF IT LOOSES
def check_lost (grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    for y in range(3):
        for x in range(3):
            if grid[y][x] == 0:                                             #check if 0 is a value of an item in teh grid
                return False
            if grid[y][x] == grid[y][x+1] or grid[y][x] == grid[y+1][x]:    #check if the adjacent values are equal
                return False
    for x in range(3):
        if grid[3][x] == grid[3][x+1] or grid[x][3] == grid[x+1][3]:        #check those which adjacent for the line 4 and  colunm 4 
            return False
        if grid[x][3] == 0 or grid[3][x] == 0:                              #check those with values 0 for the line 4 and  colunm 4 
            return False    
    
    return True
                

#CHECK IF IT WINS    
def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    for y in range(4):
        for x in range(4):
            if grid[y][x] >= 32:
                return True
    else:
        return False

#MAKE A COPY OF THE GRID
def copy_grid (grid):
    """return a copy of the grid"""
    grid_copy=[]                            #create a 1d array
    for y in range(4):
        grid_copy.append(['']*4)            #transform the 1D array to a 2D array(4x4)
        for x in range(4):
            grid_copy[y][x] = grid[y][x]    #make a copy of the grid
    return grid_copy                        #return the copy


#CHECK IF TWO GRID ARE EQUAL
def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    for y in range(4):              
        for x in range(4):
            if grid1[y][x] != grid2[y][x]:  
                return False
    else:
        return True


    
    