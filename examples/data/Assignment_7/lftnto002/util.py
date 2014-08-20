"""module of utility functions to manipulate 2-dimensional arrays of size 4x4
   Bridgette Lefatsa
   LFTNTO002
   2 May 2014"""

import copy
#Create a 4x4 grid
def create_grid(grid):
    for i in range(4):
        grid.append([])
        for j in range(4):
            grid[i].append(0)
    return grid

#print out a 4x4 grid in 5-width columns within a box
def print_grid(grid):
    string="|"
    for i in range(4):
        for j in range(4):
            if grid[i][j]==0:
                add=" "
            else:
                add=str(grid[i][j])
            string=string+add.ljust(5)
        string=string+"|\n|"
    end=len(string) -1
    string="+--------------------+\n"+string[0:end]+"+--------------------+"
    print(string)

#return True if there are no 0 values and no adjacent values that are equal; otherwise False       
def check_lost(grid):
    find="no"
    for i in range(4):
        check_grid=str(grid[i])
        for x in check_grid:
            count=0
            for j in range(4):
                if check_grid[j]==x:
                    count+=1
            if count>1:
                find="yes"
    grid_search=str(grid)   
    if (grid_search.find("0") > -1) or find=="yes":
        return "False"
    else:
        return "False"
    
#return True if a value>=32 is found in the grid; otherwise False
def check_won(grid):
    count=0
    for i in range(4):
        for j in range(4):
            if grid[i][j]>=32: 
                count+=1
    if count>0:
        return "True"
    else:
        return "False"
    
#return a copy of the grid   
def copy_grid(grid):
    new_grid=copy.deepcopy(grid)
    return new_grid

#check if 2 grids are equal - return boolean value
def grid_equal(grid1,grid2):
    count=0
    for i in range(4):
        for j in range(4):
            if grid1[i][j]==grid2[i][j]:
                count+=1
    if count==16:
        return "True"
    else:
        return "False"
    

