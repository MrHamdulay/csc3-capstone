def create_grid(grid):
    height = 4
    for i in range (height):
        grid.append ([0] * 4)    

def print_grid (grid):
    l = '{0:<5}'
    print("+--------------------+")
    num = 4
    for i in range(len(grid)):
        for j in range(len(grid)):
            if num % 4 == 0:
                print("|",end='')
            if grid[i][j] == 0:
                print(l.format(" "),end='')
            else:
                print(l.format(grid[i][j]),end='')
            num+=1
        print("|",end='')
        print()
    print("+--------------------+")
    
def check_lost (grid):
    for grid_3 in range(len(grid)):
        for grid_31 in range(len(grid)):
            if grid[grid_3][grid_31] != grid[grid_3-1][grid_31-1]:
                return True
            elif grid[grid_3][grid_31] != grid[grid_3+1][grid_31+1]:
                return True
            elif grid[grid_31][grid_3] != grid[grid_31-1][grid_3-1]:
                return True
            elif grid[grid_31][grid_3] != grid[grid_31+1][grid_3+1]:
                return True
            else:
                return False

def check_won (grid):
    for g_4 in range(len(grid)):
        for g_41 in range(len(grid)):
            if grid[g_4][g_41] >32:
                return True
            else:
                return False
            
def copy_grid (grid):
    for g_5 in range(len(grid)):
        for g_51 in range(len(grid)):
            grid[g_5][g_51]
        return grid
    
def grid_equal (grid1, grid2):
    for g_6 in range(4):
        for g_61 in range(4):
            if grid1 == grid2:
                return True
            else:
                return False