# util.py, coding basic functions used in the 2048 program
# Hendrik Joosten
# 27/04/2014

def create_grid(grid):
    """create a 4x4 grid"""
    # for loop to make a 2 dimensional array using husseins method
    for a in range(4):
        grid.append([0]*4)
    return grid


def print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    # prints the top ledge
    print("+--------------------+")
    # forloop to go through the rows
    for a in range(4):
        # forloop to go through the columns
        for b in range(4):
            #element is the number we are currently working with
            element = grid[a][b]
            # the amount of spaces so that the formatting looks correct
            gap = 5-len(str(element))
            
            # printing the emty gaps where the array contains zeros
            if element == 0:
                if b == 0:
                    print("|"," "*5,sep="",end="")
                elif b == 3:
                    print(" "*5,"|",sep="",end="")
                else:
                    print(" "*5,sep="",end="")
                    
            #printing the actual non zero elements in the grid
            else:
                if b == 0:
                    print("|",element," "*gap,sep="",end="")
                elif b == 3:
                    print(element," "*gap,"|",sep="",end="")
                else:
                    print(element," "*gap,sep="",end="")  
        # goes to newline
        print("")  
    # prints the bottom ledge
    print("+--------------------+")


def check_lost (grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    # This method checks all 4 adjacent spaces for ==
    # originally there was a problem with the border values
    # to counter this i placed the 4x4 array in the cenre of a 6x6 array 
    # to create a buffer, i filled it with ones so that there would never be false equals
    """VISUAL REPRESENTATION"""
    # [1][1][1][1][1][1]    
    # [1][X][X][X][X][1]
    # [1][X][X][X][X][1]
    # [1][X][X][X][X][1]
    # [1][X][X][X][X][1]
    # [1][1][1][1][1][1]
    
    
    # vaiables
    lost = True
    grid6x6 = []
    
    #making a 6x6 grid
    for a in range(6):
        grid6x6.append([1]*6)
        
        
    # places the 4x4 grid within the centre of the 6x6 grid  
    for b in range(4):
        for c in range(4):
            grid6x6[b+1][c+1] = grid[b][c]
            # checks for 0 element so game can continue
            if grid[b][c] == 0:
                lost = False
                
                
    # this checks all 4 adjacent blocks for ==        
    for d in range(1,5):
        for e in range(1,5):
            if grid6x6[d][e] == grid6x6[d][e+1]:
                lost = False
            if grid6x6[d][e] == grid6x6[d][e-1]:
                lost = False
            if grid6x6[d][e] == grid6x6[d+1][e]:
                lost = False
            if grid6x6[d][e] == grid6x6[d-1][e]:
                lost = False
    return lost
    
            
         
def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    won = False
    # searches for a element > = 32
    for a in range(4):
        for b in range(4):
            if grid[a][b] >= 32:
                won = True
    return won
    
    
def copy_grid (grid):
    """return a copy of the grid"""
    # makes a new grid
    new_grid = []
    for a in range(4):
        new_grid.append([0]*4)
    
    # copy values from grid into new grid
    for b in range(4):
        for c in range(4):
            new_grid[b][c] = grid[b][c]
    
    return new_grid
        

def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    equal = True
    # goes through ever element and checks ==
    for a in range(4):
        for b in range(4):
            if grid1[a][b] != grid2[a][b]:
                equal = False
                
    return equal   