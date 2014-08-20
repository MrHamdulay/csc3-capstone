grid = []

def create_grid(grid):
    for i in range(4):
        grid.append([0] * 4)
    
def print_grid(grid):
    x = "{:<5}"    
    
    print("+","-"*20,"+",sep="")    
    for i in range(4):
        print("|",end="")
        for j in range(4):
            if grid[i][j] != 0:
                print(x.format(grid[i][j]),end="")
            else:
                print(x.format(""),end="")
        print("|",end="")
        print()
    print("+","-"*20,"+",sep="")
    
def check_lost (grid):
    for i in range(len(grid)):
        for j in range(len(grid)):
            if int(grid[i][j]) == 0: 
                return False
           
    else:
        for i in range(3):
            for j in range(3):
                if (grid[i][j] == grid[i+1][j] or grid[i][j] == grid[i][j+1]):
                    return False
                #if i == grid[i][3] != grid[i][j] or grid[i][j] != grid[i][j-1]:               
               
        if grid[3][0] == grid[2][0] or grid[3][0] == grid[3][1] or grid[3][1] == grid[3][2] or grid[3][1] == grid[2][1] or grid[3][2] == grid[2][2] or grid[3][2] == grid[3][3] or grid[3][3] == grid[2][3] or grid[2][3] == grid[1][3] or grid[1][3] == grid[0][3] or grid[0][3]==grid[0][2] or grid[1][3] == grid[1][2] or grid[2][3] == grid[2][2] or grid[3][3] == grid[3][2]:                        
            return False
        else: return True
     
def check_won(grid):
    for i in range(4):
            for j in range(4):
                if grid[i][j] >= 32:
                    return True
    return False
        
    
        
def copy_grid (grid):
    new_grid = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    for i in range(len(new_grid)):
        for j in range(len(new_grid)):
            new_grid[i][j] = grid[i][j]
                
    return new_grid

def grid_equal (grid1, grid2):
    test = False
    count = 0
    for i in range(4):
        if grid1[i] == grid2[i]:
            count+=1
        
    if count == 4:
        test = True
        return test
    else: return test
    
    
            
            