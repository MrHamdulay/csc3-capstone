'''program to manipulate 2-dimensional arrays of size 4x4
Thabiso Beau
30 April 2014
Assignment 7: #util.py'''

grid=[] #empty list, so we append the values to it to create 2-d list
#creating the grid
def create_grid(grid): 
    for i in range(4): #creating list for printing borders - using multi-dimensional array function
        grid.append([0]*4)
create_grid(grid)

#creating the inner values for the grid
def print_grid(grid):
    print('+'+('-'*20)+'+')#prints outside border
    for j in range(4): #we're indexing the outside part of the outside list  - #j = row
        print('|', end='')
        for a in range(4):#we're indexing the inner part of the list - #a = column 
            if grid[j][a]==0:
                print(' '.ljust(5), end='')
            else:
                print("{0:<5}".format(grid[j][a]), end='')#ending with a empty string to stop it printing on new lines
        print('|', end='')
        print()
    print('+'+('-'*20)+'+') #prints outside border

def check_lost(grid):
    for a in range(4):
        for j in range(4):
            if grid[j][a] == 0:
                return False
            if j >0:   #checking for one before and one after the position in the row and whether they're not equal to the actual position in the grid
                if grid[j-1][a] ==grid[j][a]: 
                    return False #then the user can still continue with the game
            if j+1<4:
                    if grid[j+1][a] == grid[j][a]:
                        return False
            if a>0:    
                if grid[j][a-1] == grid[j][a]: #checking for one before and one after the position in the column and whether they're not equal to the actual position in the grid
                    return False #then the user can still continue with the game
            if a+1<4:    
                if grid[j][a+1] == grid[j][a]:
                    return False
    return True    #the user has lost

def check_won(grid):#checking for values that are >=32
    for j in range(4): #outside value a.k.a. row value 
        for a in range(4): #inner value a.k.a. column value
            if grid[j][a] >=32: #index an actual value
                return True 
    return False #if the conditions are not met by the nested loop

def copy_grid(grid):
    #create 2nd grid to test equality
    grid2 = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]] #2nd grid created with 2-d arrays
    for j in range(4):
        for a in range(4):
            grid2[j][a] = grid[j][a]
    return grid2

#test equality of grids by using boolean 'True'or 'False' operators -- could possibly bool(expr)
def grid_equal(grid, grid2):
    if grid == grid2:
        return True
    else:
        return False
 #Ask tutor as to whether program is supposed to be invoked or Automatic Marker will do that?