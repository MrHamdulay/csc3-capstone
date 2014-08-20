#Question2
#Tase Ngambi
#28 April 2014

def create_grid(grid):
    for x in range(4):
        grid.append([0]*4)     
        
   
def print_grid(grid):
    
    tmp =""
    rowlen =[]
    for x in range(4):
        tmp =""
        for j in range(4):
            tmp = tmp+str(grid[x][j]) 
        rowlen.append(len(tmp))
    width = max(rowlen)
    
    
    if width <= 5:    
        print("+","-"*(17+(width-1)),"+", sep ="")  
    else:
        print("+","-"*(17+(width-4)),"+", sep ="") 
        
    #|     16        128  |
    #|xxxxx16xxxxx
    for x in range(4):
        print("|",end="")
        for y in range(4):
            if grid[x][y] == 0:
                print(" ", "", sep =" "*(5-len(str(grid[x][y]))), end = "")
            else:
                print(grid[x][y], "", sep =" "*(5-len(str(grid[x][y]))), end = "")
        print("|", end ="")
        print()   
    if width <= 5:    
        print("+","-"*(17+(width-1)),"+", sep ="")  
    else:
        print("+","-"*(17+(width-4)),"+", sep ="") 
        
    
    
def check_lost(grid):
    test = False
    cond = 0
    cond2 = 0
    for i in range(4):
        for x in range(4):
            if grid[i][x] == 0:
                cond = 1
    
    for i in range(3):
        for x in range(3):    
            if grid[i][x] == grid[i][x+1]:
                cond2 = 1
            elif grid[i][x] == grid[i+1][x]:
                cond2 =1
                
    if cond ==0 and cond2 == 0:
        return True
    
    else:
        return False
        
def check_won(grid):
    for i in range(4):
        for x in range(4):   
            if grid[i][x] >= 32:
                return True
    else:
        return False
    
def copy_grid(grid):
    import copy
    copy_grid = copy.deepcopy(grid)
    return copy_grid

def grid_equal(grid1, grid2):
    for x in range(4):
        for i in range(4):
            if grid1[x][i] != grid2[x][i]:
                return False
    else:
        return True
            
            
    
    
            
    



 

 