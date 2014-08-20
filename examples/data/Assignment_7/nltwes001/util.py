#ASSIGNMENT 7
#QUESTION 3
#NLTWES001

def create_grid(grid):
    for i in range(4):
        grid.append([0]*4)
        
def print_grid(grid):
    print("+","-"*20,"+",sep="")
    for row in range(4):
        for col in range(4):
            if col==0:
                print("|",end="")            
            if grid[row][col]==0:
                print(" "*5,sep="",end="")
            if grid[row][col] != 0:
                print(grid[row][col]," "*(5-len(str(grid[row][col]))),sep="",end="")
            if col==3:
                print("|",end="")            
        print()
    print("+","-"*20,"+",sep="")
    
def check_lost (grid):
    x = True
    for row in range (4):
        for col in range(4):
            left = col-1         
            right = col+1
            top = row-1
            bot = row+1           
            if grid[row][col] == 0: #all Zeros
                return False
            elif row == 0 and col == 3: #top right : no right or top
                if grid[row][col] == grid[bot][col] or grid[row][col] == grid[row][left]: 
                    return False
            elif row == 0 and col == 0:#top left  : no left or top
                if grid[row][col] == grid[bot][col] or grid[row][col] == grid[row][right]:
                    return False
            elif row == 3 and col == 0:   #bottom left: no bot or left
                if grid[row][col] == grid[top][col] or grid[row][col] == grid[row][right]:
                    return False
            elif row == 3 and col == 3:  #bottom right: no bot or right
                if grid[row][col] == grid[top][col] or grid[row][col] == grid[row][left]:
                    return False            
            elif row == 0:  #top: no top
                if grid[row][col] == grid[bot][col] or grid[row][col] == grid[row][left] or grid[row][col] == grid[row][right]:
                    return False
            elif row == 3: #bot: no bot
                if grid[row][col] == grid[top][col] or grid[row][col] == grid[row][left] or grid[row][col] == grid[row][right]:
                    return False    
            elif col == 0: #left: no left
                if grid[row][col] == grid[row][right] or grid[row][col] == grid[top][col] or grid[row][col] == grid[bot][col]:
                    return False
            elif col == 0: #right: no right
                if grid[row][col] == grid[row][left] or grid[row][col] == grid[top][col] or grid[row][col] == grid[bot][col]:
                    return False  
    return True

def check_won(grid):
    won=False
    for row in range(4):
        for col in range(4):    
            if grid[row][col]>=32:
                won=True
    return won

import copy
def copy_grid(grid):
    gridcopy = copy.deepcopy(grid)
    return gridcopy    

def grid_equal (grid1, grid2):
    if grid1==grid2:
        return True
    else:
        return False

