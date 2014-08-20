
def create_grid(grid):
    for y in range(4):
        grid.append([0]*4)
    return grid
        
#print grid
def print_grid (grid):
    #print out a 4x4 grid in 5-width columns within a box
    print("+--------------------+")
    for i in grid:
        print('|', end='')
        for j in i:
            j = str(j)
            if j == '0':
                print(' '.ljust(5), end = '')
            else:
                print(j.ljust(5),end = '')
        print('|')
    print("+--------------------+")        

#checks to see if their are no more valid moves availiable
def check_lost (grid):
    for i in range(len(grid)-1):
        for j in range(len(grid[i])-1):
            if grid[i][j] == 0:
                return False
            elif grid[i][j] == grid[i+1][j]:
                return False
            elif grid[i][j] == grid[i][j+1]:
                return False
    return True


def check_won(grid):            #returns true if a value greater than 32 is on the board
    for x in grid:
        for y in x:
            if y>=32:
                return True
    else:
        return False

def grid_equal(grid1, grid2):           #checks to see if the 2 grids sent to it are identical
    if grid1==grid2:
        return True
    else:
        return False
    
def copy_grid(grid):                #returns a copy of the parameter grid
    GridCopy=[]
    for position in grid:
        GridCopy.append(list(position))
    return GridCopy


    
                    
            
            
            
        
            
        
        


   
            
   