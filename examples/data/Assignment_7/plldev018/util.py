#Creating and printing grids
#Devaksha Pillay
#27 April 2014

def create_grid(grid):
    # create a 4 by 4 grid
    for rows in range(4):
        grid.append([0]*4)

def print_grid(grid):
    #print 2D grid
    print("+","-"*20,"+", sep = "")    
    for rows in range(4):
        for columns in range(6):
            if columns == 0:
                print("|",sep = "", end = "")
            elif 1<=columns<5:
                if grid[rows][columns-1] == 0:
                    print("{0:<5}".format(" "), sep = "", end = "")
                else:
                    print("{0:<5}".format(grid[rows][columns-1]), sep = "", end = "" )
    print("+","-"*20,"+", sep = "")

def check_lost(grid):

    for rows in range(4):
        for columns in range(4):
            
            #variables to check adjacent values
            l = columns - 1
            r = columns + 1
            t = rows - 1
            b = rows + 1
            
            #variable checking the value of a specific cell
            value = grid[rows][columns]            
            
            #check for the empty spaces
            if value == 0:
                return False
            
            #check the top left value
            elif rows == 0 and columns == 0:
                if value == grid[rows][r] or value == grid[b][columns]:
                    return False
                
            #check the bottom left value
            elif rows == 3 and columns == 0:
                if value == grid[t][columns] or value == grid[rows][r]:
                    return False
                
            #check the top right value
            elif rows == 0 and columns == 3:
                if value == grid[rows][l] or value == grid[b][columns]:
                    return False
                
            #check the bottom right value
            elif rows == 3 and columns == 3:
                if value == grid[rows][l] or value == grid[t][columns]:
                    return False
                
            #in the first column
            elif columns == 0:
                if value == grid[t][columns] or value == grid[b][columns] or value == grid[rows][r]:
                    return False
                
            #in the last column
            elif columns == 3:
                if value == grid[t][columns] or value == grid[b][columns] or value == [rows][l]:
                    return False
            
            #in the top row
            elif rows == 0:
                if value == grid[b][columns] or value == grid[rows][l] or value == grid[rows][r]:
                    return False
            
            #in the bottom row
            elif rows == 3:
                if value == grid[t][columns] or value == grid[rows][l] or value == grid[rows][r]:
                    return False
            
            #check every other value
            elif value == grid[t][columns] or value == grid[b][columns] or value == grid[rows][r] or value == grid[rows][l]:
                return False
            
            #no more moves
            #game over
            else:
                return True

def check_won(grid):
    #check per row and column
    for rows in range (4):
        for columns in range (4):
            #game won if there is a value over 32
            if grid[rows][columns]>=32:
                return True
    return False

#to create a copy of the grid
import copy

def copy_grid(grid):
    new_grid = copy.deepcopy(grid)
    return new_grid

def grid_equal (grid1, grid2):
    counter = 0
    for rows in range(4):
        for columns in range(4):
            if grid1[rows][columns] == grid2[rows][columns]:
                counter = counter + 1
        if counter == 16:
            return True
        else:
            return False