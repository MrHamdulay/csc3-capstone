#Phumelele Ndimande
#Assignment 7

global grid
grid = []

def create_grid(grid): 
    """create a 4x4 grid"""
    
    for y in range(4):
        row = []
        for x in range(4):
            row.append(0)
        grid.append(row)
    
#grid1 = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]    

def print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    print("+",20*"-","+",sep="")
    for i in range(4):
        print("|",end="")
        for num in grid[i]:
            if num == 0:
                print("{0:<5}".format(" "), end="")
            else:
                print("{0:<5}".format(num), end="")
        print("|")
    print("+",20*"-","+",sep="")

def check_lost (grid):
    """This program will check if game is lost. returns True if there are non 0 values and no adjacent values that are equal; otherwise False"""
    for i in range(4):
        #Looks for 0 values and returns false if found
        for num in range(4):
            if grid[i][num] == 0:
                return False
            #Looks for horizontal adjacent values that are equal and will return false if found
        for num in range(3):
            if grid[i][num] == grid[i][num+1]:
                return False
        #Looks for vertical adjacent values that are equal and will return false if found
    for i in range(3):
        for num in range(4):
            if grid[i][num] == grid[i+2][num]:
                return False
            #if none of the conditions are met will return True
    return True     


def check_won (grid):
    """If game is won it will return True if a value>=32 is found in the grid; otherwise will return False"""
    for i in grid: #Loops through all elements in the grid
        for a in i:
            if a >= 32:
                return True
    return False        

def copy_grid (grid):
    """return a copy of the grid"""
    
    new_grid =[]
    
    for i in grid:
        new_row = []
        for a in i:
            new_row.append(a)
        new_grid.append(new_row)
        
    return new_grid #returns the copy

def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    
    for i in range(4):
        for num in range(4):
            if grid1[i][num] != grid2[i][num]:
                return False #if corresponding values in grid match
        
    return True 