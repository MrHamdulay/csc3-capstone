#Utility
#Sofia Palmer
#29 April 2014

def create_grid(grid):
    height = 4
    grid = []
    for i in range(height):
        grid.append([ ] * 4)
    return grid

def print_grid (grid):  
    print("+",21*"-","+", sep = "")
    height = 4
    for row in range(height):
        print("|", end = " ")
        for col in range(height):
            print(grid[row][col], end = (5-len(str(grid[row][col]))) * " ")
        print("|")
    print("+",21*"-","+", sep = "")

def check_lost (grid):
    height = 4
    for row in range(height):
        for col in range(height):
            if (grid[row][col] == 0):
                return False
            if (col < len(grid)):
                if (grid[row][col] == grid[row][col+1]):
                    return False
            if (row < len(grid)):
                if (grid[row][col] == grid[row+1][col]):
                    return False
        else:
            return True

def check_won (grid):
    height = 4
    for row in range(height):
        for col in range(height):
            if (grid[row][col] >= 32):
                return True
            else:
                return False    

def copy_grid (grid):  
    height = 4
    grid = []
    for i in range(height):
        grid.append([ ] * 4)
    return grid


def grid_equal (grid1, grid2):
    for row in range(len(grid1)):   
        for col in range(len(grid2)):
            if (grid1[row][col] != grid2[row][col]):
                return False
    return True       
         




            
    