"""Utility Program
Richard Marais
14/05/02"""

from copy import deepcopy

def create_grid(grid):   #create grid program, appends 0's into a list
    k = 0
    for i in range(4):
        grid.append([])
    for h in grid:
        for j in range(4):
            grid[k].append(0)
        k+=1



def print_grid(grid):         #print grid function
    print("+--------------------+")          #top of grid
    for i in grid:
        strin=''
        for j in i:
            if j == 0:
                j = ' '               #adding the values to the list as strings and formatting into columns
            fmat = "{0: <5}"
            j = fmat.format(str(j))
            strin+=str(j)
        print("|",strin,"|",sep='')
    print("+--------------------+")

def check_lost (grid):              #check for 0's and adjacent values the same
    z = 0
    for i in grid:
        x = 1                            
        for j in i:
            if j == 0:                   #check for 0s
                return False
            if x != 4:         
                if j == grid[z][x] or j == grid[z-1][x]:           #check for  adjacent values the same
                    return False
            
            x = x+1
        z = z+1 
    return True


def check_won (grid):           #check if won
    for i in grid:
        for j in i:             
            if j >= 32:        #checking for a value abov 32, = true
                return True
    return False           #else false
    
def copy_grid(grid):            #copy grid function
    return deepcopy(grid)

def grid_equal (grid1, grid2):              #checking two grids are equal
    if grid1 == grid2:           #if equal return true
        return True
    else:
        return False

