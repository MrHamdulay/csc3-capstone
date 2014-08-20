"""Module of utility functions
Sithasibanzi Kondleka
01 May 2014"""

def create_grid(grid):
    #creating a 4x4 grid
    height = 4
    for i in range (height):
        grid.append ([0] * 4)
        
def print_grid(grid):
    print("+--------------------+") #top border
    for i in range(4):
        for j in range(4):
            gap = 5-len(str(grid[i][j])) #make gaps 5 minus the length of the number
            if j != 3:
                if j ==0 and grid[i][j] == 0:
                    print("|",' '," "*gap, end="",sep="")
                elif j==0:
                    print("|",grid[i][j]," "*gap, end="",sep="")
                else:
                    if grid[i][j] == 0:
                        print(' '," "*gap, end="",sep="")
                    else:
                        print(grid[i][j]," "*gap, end="",sep="")
            else:
                if grid[i][j] == 0:
                    print(' '," "*gap, end="|\n",sep="")
                else:
                    print(grid[i][j]," "*gap, end="|\n",sep="")                
    print("+--------------------+") #bottom border
            
#print_grid([[2,0,2,0],[0,4,0,8],[0,16,0,128],[2,2,2,2]])


def check_lost (grid):
    for i in range(3):
            for j in range(3):
                if grid[i][j] ==0:
                    return False
                elif grid[i][j] == grid[i][j+1]:
                    return False
                elif grid[i][j] == grid[i+1][j]:
                    return False
            return True
                
def check_won (grid):
    for i in range(4):
            for j in range(4):
                if grid[i][j] >=32:
                    return True
    return False

def copy_grid (grid):
    
    height = 4
    for i in range (height):
        grid2.append ([0] * 4)
    for x in range(4):
        for y in range(4):
            new_grid[x][y] = grid[x][y]
    return new_grid

def grid_equal (grid1, grid2):
    for x in range(4):
        for y in range(4):
            if grid1[x][y] != grid2[x][y]:
                return False
    return True