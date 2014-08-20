"""Functions for 2048 Program
Geoff Murphy
MRPGEO001
01 May 2014"""

def create_grid(grid):   #Creates a grid
    grid.append([0,0,0,0])
    grid.append([0,0,0,0])
    grid.append([0,0,0,0])
    grid.append([0,0,0,0])
    
    

def print_grid(grid):
    
    print('+--------------------+')

    for j in grid:
        print('|', end = "")
        if j[0] != 0:
            print('{0:<5}'.format(j[0]), end = "")   #Prints each item in the nested list with a formatted space of 5
        else:
            print('{0:<5}'.format(" "), end = "")    #If the item is a zero, a space is printed
        if j[1] != 0:
            print('{0:<5}'.format(j[1]), end = "")
        else:
            print('{0:<5}'.format(" "), end = "")
        if j[2] != 0:
            print('{0:<5}'.format(j[2]), end = "")
        else:
            print('{0:<5}'.format(" "), end = "")
        if j[3] != 0:
            print('{0:<5}'.format(j[3]), end = "")
        else:
            print('{0:<5}'.format(" "), end = "")
        print('|')
        
    print('+--------------------+')
            
def check_lost(grid):
  
    if 0 in grid[0]:        #Returns false if a 0 exists
        return False
    elif 0 in grid[1]:
        return False
    elif 0 in grid[2]:
        return False
    elif 0 in grid[3]:
        return False
    
    elif grid[0][0] == grid[0][1]:      #Checks each value against its adjacent values and sees whether they are equal or not. Returns True if they are
        return True
    elif grid[0][1] == grid[0][2]:
        return True
    elif grid[0][2] == grid[0][3]:
        return True
    
    elif grid[1][0] == grid[1][1]:
        return True
    elif grid[1][1] == grid[1][2]:
        return True
    elif grid[1][2] == grid[1][3]:
        return True
    
    elif grid[2][0] == grid[2][1]:
        return True
    elif grid[2][1] == grid[2][2]:
        return True
    elif grid[2][2] == grid[2][3]:
        return True
    
    elif grid[3][0] == grid[3][1]:
        return True
    elif grid[3][1] == grid[3][2]:
        return True
    elif grid[3][2] == grid[3][3]:
        return True        
    
    elif grid[0][0] == grid[1][0]:
        return True
    elif grid[1][0] == grid[2][0]:
        return True
    elif grid[2][0] == grid[3][0]:
        return True
    
    elif grid[0][1] == grid[1][1]:
        return True
    elif grid[1][1] == grid[2][1]:
        return True
    elif grid[2][1] == grid[3][1]:
        return True  
    
    elif grid[0][2] == grid[1][2]:
        return True
    elif grid[1][2] == grid[2][2]:
        return True
    elif grid[2][2] == grid[3][2]:
        return True 
    elif grid[0][3] == grid[1][3]:
        return True
    elif grid[1][3] == grid[2][3]:
        return True
    elif grid[2][3] == grid[3][3]:
        return True      
    else:
        return False   
    

def check_won(grid):
    minimum = 32        #Checks if a number greater or equal to 32 exists or not. Returns True if one does
    for i in grid:
        for j in i:
            if j >= 32:
                return True
    return False


def copy_grid(grid):
    grid = grid          #Makes a copy of the grid by going through each value in the original list and appending it to the new list
    test_grid = []
    for i in grid:
        test_grid.append(i)
    return test_grid

    
    
    
def grid_equal(grid1, grid2):
    if grid1 == grid2:        #Checks if 2 grids are equal or not, and returns True if they are
        return False
    else:
        return True
    