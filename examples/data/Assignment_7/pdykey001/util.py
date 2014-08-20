"""
Keyoolin Padayachee
Utility of Functions
01 May 2014
"""

#Appends to a given grid to create a 4X4 list
def create_grid(grid):
    for i in range(4):
        grid.append([])
        for j in range(4):
            grid[i].append(0)
    
    return grid
#Prints a 4x4 list within a box
def print_grid(grid):
    print("+--------------------+")
    for i in range(4):
        print("|",end="")
        for j in range(4):
            if grid[i][j]==0:
                print ("{0:<5}".format(" "),end="")
            else:
                print("{0:<5}".format(grid[i][j]),end="")
        print("|")
        
    print("+--------------------+")
#Checks whether there are 0 values in the grid and if there are no more moves
def check_lost(grid):
    # checks for 0s
    zero = False
    for i in range(4):
        for j in range(4):
            if grid[i][j] == 0:
                zero = True
                return False
    #Checks if there are still legal moves            
    if zero == False :   
        for i in range(4):
            for j in range(4):
                if i == 0:
                    if j == 0:
                        if grid[i][j]!=grid[i+1][j] and grid[i][j]!=grid[i][j+1]:
                            test1 = True
                        else: test1 = False
                    elif j == 3:
                        if grid[i][j]!=grid[i+1][j] and grid[i][j]!=grid[i][j-1]:
                            test2 = True
                        else: test2 = False
                    elif grid[i][j]!=grid[i+1][j] and grid[i][j]!=grid[i][j+1] and grid[i][j]!=grid[i][j-1]:
                        test3 = True
                    else: test3 = False
                    
                elif i == 3:
                    if j == 0:
                        if grid[i][j]!=grid[i-1][j] and grid[i][j]!=grid[i][j+1]:
                            test4 = True
                        else: test4 = False
                    elif j == 3:
                        if grid[i][j]!=grid[i-1][j] and grid[i][j]!=grid[i][j-1]:
                            test5 = True
                        else: test5 = False
                    elif grid[i][j]!=grid[i-1][j] and grid[i][j]!=grid[i][j+1] and grid[i][j]!=grid[i][j-1]:
                        test6 = True 
                    else: test6 = False
                elif j == 0:
                    if grid[i][j]!=grid[i-1][j] and grid[i][j]!=grid[i][j+1]:
                        test7 = True
                    else: test7 = False
                elif j == 3:
                    if grid[i][j]!=grid[i-1][j] and grid[i][j]!=grid[i][j-1]:
                        test8 = True
                    else: test8 = False
                elif grid[i][j]!=grid[i-1][j] and grid[i][j]!=grid[i][j+1] and grid[i][j]!=grid[i][j-1]:
                    test9 = True 
                else: test9 = False
        if test1 == False or test2 == False or test3 == False or test4 == False or test5 == False or test6 == False or test7 == False or test8 == False or test9 == False:
            return False
        else: return True
#checks if player has won the game                
def check_won(grid):
    for i in range(4):
        for j in range(4):
            if grid[i][j] >= 32:
                return True
    else : return False
#Copies the list into a secondary list
def copy_grid(grid):
    copy = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    for i in range(4):
        for j in range(4):    
            copy[i][j] = grid[i][j]
    return copy
#Checks if 2 grids are the same
def grid_equal(grid1,grid2):
    if grid1 == grid2:
        return True
    else : return False
    