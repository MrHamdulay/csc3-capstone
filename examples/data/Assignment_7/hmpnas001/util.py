
"""program to write game
nasonkwe hampwaye
2014/04/30"""
grid=[]
height=4
#for row in range(height):
    #for col in range(height):
        #if "0" in grid:
            #grid.remove(0)
            #grid.insert(grid[row][col]," ")
                 
def create_grid(grid):
    #create 4X4 grid
    
    for i in range(height):
        grid.append ([0]*4)
        
def print_grid (grid):
    #print out 4X4 grid in 5-width columns within a box
    print("+","-"*20,"+",sep='')
    for row in range(height):
        print("|",end='')
        for col in range (height):
            if grid[row][col]!=0:
                print("{0:<5}".format(grid[row][col]),end='')
            else:
                print("     ",end='')
        print("|",end='')
        print()
    print("+","-"*20,"+",sep='')
    


def check_lost (grid):
    #return True if there are no 0 values and no adjacent values
    for row in range(height):
        for col in range(height):
            if grid[row][col]!=0:
                return False
            elif grid[row][col]==grid[row][col+1]:
                return False
            elif grid[row][col]==grid[row+1][col]:
                return False
        else:
            return True
            
def check_won (grid):
    #return True if a value>=32 is found in the grid; otherwise
    won=False
    for row in range(height):
        for col in range(height):
            if grid[row][col]>=32:
                won=True
    if won:
        return True
    else:
        return False
    
    
def copy_grid (grid):
    #return a copy of the grid
    import copy
    return copy.deepcopy(grid)

def grid_equal (grid1, grid2):
    for row in range(height):
        for col in range(height):
            if grid1[row][col]!=grid2[row][col]:
                return False
            else:
                return True
                        
    
    
    
       
        