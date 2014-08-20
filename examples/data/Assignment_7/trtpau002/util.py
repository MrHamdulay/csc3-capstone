"""Functions for 2048 game
Paul Truter
29 May 2014"""

#create 4X4 grid
def create_grid(grid):
    height = 4
    for i in range (height):
        grid.append ([0] * 4)
        
#print out grid
height = 4
def print_grid(grid):
    print("+" + "-"*20 + "+")    
    for row in range(height):
        print("|",end="")
        for col in range(height):
            if grid[row][col] == 0:
                    print(" "*5,end="")
            else:
                print("{0:<5}".format(str(grid[row][col])),end="")
        print("|")
    print("+" + "-"*20 + "+")

#check if player lost
def check_lost(grid):
    for row in range(height):
        for col in range(height):
            if grid[row][col] != 0:
                return False
            else:
                return True           
            for i in range(4):
                if grid[i][0] != grid[i][1] or grid[i][1] != grid[i][2] or grid[i][2] != grid[i][3]:
                    return True
                elif grid[0][i] != grid[1][i] or grid[1][i] != grid[2][i] or grid[2][i] != grid[3][i]:
                    return True
                else:
                    return False

#check if player won
def check_won(grid):
    for row in range(height):
            for col in range(height):
                if grid[row][col] >= 32:
                    return True
    return False
                
#return copy of grid
def copy_grid(grid):
    grid2 = []
    height = 4
    for i in range (height):
        grid2.append ([0] * 4)
    
    for row in range(height):
        for col in range(height):
            grid2[row][col] = grid[row][col]
    return grid2

#check if the 2 grids are equal
def grid_equal(grid, grid2):
    if grid == grid2:
        return True
    else:
        return False 
