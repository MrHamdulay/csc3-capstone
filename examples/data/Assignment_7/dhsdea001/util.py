#Question 2 
#Creating the util functions
#By: Dean de Haast
import copy
def create_grid(grid):
    """create a 4x4 grid"""
    for i in range (4):
        grid.append([0]*4)
       
def print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    print("+","-"*20,"+", sep ="")
    for i in grid: 
        print("|",end='') 
        for x in i: 
            x=str(x) #needed as a string for the left justification
            if x=="0": 
                print(" ".ljust(5),end="") 
            else: 
                print(x.ljust(5),end="") 
        print("|")
    print("+","-"*20,"+", sep ="")


def check_lost (grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    #searches each individual spot in the list
    for i in range(4):
        for x in range(4):
            #check for zeros
            if grid[i][x]==0: 
                return False
    for i in range(4):
        for x in range(3):
            #check if the value = value to the right
            if grid[i][x]==grid[i][x+1]:
                return False
    for i in range(3):
        for x in range(4):
            #check if the value = value below
            if grid[i][x]==grid[i+1][x]:
                return False
    return True    

def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    #searches each individual spot in the list
    
    for i in range(4):
        for x in range(4):
            if grid[i][x]>31:
                return True

    return False   

def copy_grid (grid):
    """return a copy of the grid"""
    CopyGrid=copy.deepcopy(grid)
    return CopyGrid    

def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    for i in range(len(grid1)):
        for x in range(len(grid1[i])):
            if grid1[i][x]==grid2[i][x]:
                continue
            else:
                return False
    return True    