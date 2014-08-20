# util.py
# author: bxtnaa002
# assignment 7


def create_grid(grid):
    #create a 4x4 grid
    for i in range(4):
        grid.append([0]*4)

def print_grid (grid):
    #print out a 4x4 grid in 5-width columns within a box
    print ("+"+"-"*20+"+") #print out border of grid
    for i in range(4):
        print ("|",end='')
        for s in range(4):
            if grid[i][s] == 0:
                print ("     ",end='')
            else:
                print (str(grid[i][s])+(" "*(5-len(str(grid[i][s])))),end='')#used to get it into 5 width columns 
        print ("|")
    print ("+"+"-"*20+"+")#print bottom border
    
def check_lost (grid):
    #return True if there are no 0 values and no adjacent values that are equal; otherwise False
    same = 0
    zero = 0
    for i in range(3):
        for s in range(1,4):
            if grid[i][s] == grid[i][s-1] or grid[i][s] == grid[i+1][s]: #check if there are adjacent values equal in adjacent columns or rows
                same+=1
                break
   
    for i in range(4):
        if 0 in grid[i]:#check if there are 0 values
            zero+=1
            break
    if same==0 and zero==0:
        return True
    else:
        return False
            
def check_won (grid):
    #return True if a value>=32 is found in the grid; otherwise False
    won = 0
    for i in range(4):
            for s in range(4):
                if grid[i][s] >= 32:
                    won +=1
                    break
    if won == 0:
        return False
    else:
        return True
                
def copy_grid (grid):
    #return a copy of the grid
    gridnew = []
    for i in range(4):
        gridnew.append([0]*4)
    for i in range(4):
        for s in range(4):
            gridnew[i][s] = grid[i][s]
    return gridnew

def grid_equal (grid1, grid2): #check if 2 grids are equal - return True if equal and False if not equal
    if grid1 == grid2:
        return True
    else:
        return False