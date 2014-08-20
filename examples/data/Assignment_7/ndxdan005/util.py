

def create_grid(grid):
    for i in range(4):
        grid.append([0]*4) 
def print_grid(grid):
    print('+--------------------+') 
    for row in range(4):
        print('|',end = '') 
        for col in range(4): #nested for loop to iterate through each variable
            if grid[row][col] == 0: #check if element in grid equals 0
                    print('{:<5}'.format(' '),end = '') #fills 0 with fives spaces
            else:
                print('{:<5}'.format(grid[row][col]),end = '') #otherwise prints numeric element
        print('|')
    print('+--------------------+')
    
def check_lost(grid):
    lost = True 
    for row in grid:
        if 0 in row:
            lost = False #if there are any 0's, have not lost the game yet
    for row in range(4): #right adjacent
        for col in range(3):
            if grid[row][col] == grid[row][col + 1]:
                lost = False #have not lost if number to the right is the same
        
        for col in range(1,4): #left adjacent
            if grid[row][col] == grid[row][col - 1]:
                lost = False #have not lost if number to the left is the same
    
    for row in range(3): #bottom adjacent
        for col in range(4):
            if grid[row][col] == grid[row + 1][col]:
                lost = False #have not lost if number below is the same
            
    for row in range(1,4): #top adjacent
        for col in range(4):
            if grid[row][col] == grid[row - 1][col]:
                lost = False #have not lost if number above is the same
    
    return lost #returns boolean statement

def check_won(grid):
    won = False
    for row in range(4):
        for col in range(4): #iterate through all elements in grid
            if grid[row][col] >= 32: #if element greater than equal to 32, the game has been won
                won = True 
    
    return won

import copy
def copy_grid(grid):
    grid_copy = copy.deepcopy(grid) #in order to make an un-referenced copy of the grid
    return grid_copy

def grid_equal(grid1,grid2):
    equal = True
    for row in range(4):
        for col in range(4): #iterates through all elements in the grid
            if grid1[row][col] == grid2[row][col]:
                continue #if element from grid1 is equal to element from grid2, continue with iteration
            else:
                equal = False #if 2 elements differ, changes boolean allocation
    
    return equal 
            
    