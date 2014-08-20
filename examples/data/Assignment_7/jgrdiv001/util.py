""""Assinment 7 question2
program to create utility functions that can be used
author : Divan Jagers
27 April 2014"""

import copy
def create_grid(grid):
    """create a 4X4 grid"""
    for i in range(4):
        grid.append([0]*4)
def print_grid(grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    print("+"+"-"*20+"+")
    for i in grid:
        print('|',end='')
        for item in i: # a loop to make each item a string
            item=str(item)    #creates a string value
            if item=='0':
                print(' '.ljust(5),end='')    #justifies each value to left by 5 units
            else:
                print(item.ljust(5),end='')   #it tyhen prints each of these items 
        print('|')        
        
    print("+"+"-"*20+"+")   #prints the border values
 
def check_lost(grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    for i in range(len(grid)-1):
        for j in range(len(grid[i])-1):
            #check if there are zeros
            if grid[i][j]==0: 
                return False
            #check if the value to the right equals the value
            elif grid[i][j]==grid[i][j+1]:
                return False
            #check if the value above equals value
            elif grid[i][j]==grid[i+1][j]:
                return False
    else:
        return True   #if none of these are valid then the game can continue 
def check_won(grid):
    for i in range(4):
        for j in range(4):
            if grid[i][j]== "":   #if the grid is perhaps an empty string
                grid[i][j]=0      #else the value then becomes zero
            if grid[i][j] >= 32:    #if any value in the grid id above 32,the game is won
                return True
    return False
def copy_grid(grid):
    new_grid=copy.deepcopy(grid)   #creates a deep copy of the original grid
    return new_grid
def grid_equal(grid1,grid2):
    if grid1==grid2:       #if the two grid are exactly alike, then return True
        return True
    else:
        return False
    