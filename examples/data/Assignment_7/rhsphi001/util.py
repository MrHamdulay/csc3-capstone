'''Phillip Ruhesi
01/05/2014
list of functions necessary to manipulate a grid'''
import copy
def create_grid(grid):
    #grid = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]         #2D array
    for i in range(4):
        grid.append('0000')
        
def print_grid (grid):
    print('+','-'*20,'+',sep='')
    for y in range(len(grid)):
        print('|',end='')
        for x in range(len(grid)):
            if grid[y][x]!=0:
                print("{0:<5}".format(grid[y][x]),end='')   #Prints the value of grid[y][x] left justified and width of 5
            else:
                print(' '*5,end='')
    
        print('|')
    print('+','-'*20,'+',sep='')    

def check_lost (grid):
   #check for 0 in the grid
    for y in range(4):
        for x in range(4):
            if grid[y][x]==0:     
                return False
            else:
                continue
                
    #check for horizontal adjacent values that are equal
    for y in range(3):
        for x in range(4):
            if grid[y][x]==grid[y+1][x]:
                return False
            else:
                continue
    #check for vertical adjacent values that are equal
    for y in range(4):
        for x in range(3):
            if grid[y][x]==grid[y][x+1]:
                return False
            else:
                continue
    return True
                
def check_won (grid):
    #check for a value greater than 32 in the grid
    for y in range(4):
        for x in range(4):
            if grid[y][x]>=32:
                return True
    return False
        
def copy_grid (grid):    
    #copy the values from original grid
    return copy.deepcopy(grid)

def grid_equal(grid1,grid2):
    #check if the grids are equal and return True or False
    return grid1==grid2

