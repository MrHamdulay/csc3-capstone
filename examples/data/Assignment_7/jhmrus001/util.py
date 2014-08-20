#RusselJay :)

def create_grid(grid):
    h=4
    for a in range(h):
        grid.append([0]*4)


def print_grid(grid):
    print("+","-"*20,"+",sep="") 
    ht=4
    for a in range(h):
        grid.append([0]*4) 
    for i in range(h):
        print("|",end="") 
        for column in range(h):
            if grid[i][column]==0: 
                print(" ".ljust(5),end="") 
            else:
                print(str((grid[i][column])).ljust(5),end="") 
        print("|",end="") 
        print()
    
    print("+","-"*20,"+",sep="") 

    
def check_lost(grid):
    
    for i in range(4):
        for j in range(4):
            if grid[i][j]==0:
                return False
            else:
                if i-1 >= 0: 
                    if grid[i-1][j]==grid[i][j]: 
                        return False
                if i+1<=3: 
                    if grid[i+1][j]==grid[i][j]:  
                        return False
                if j-1>=0:
                    if grid[i][j-1]==grid[i][j]: 
                        return False
                if j+1<=3: 
                    if grid[i][j+1]==grid[i][j]: 
                        return False
    return True 

def check_won(grid):
    for i in range(4):
        for j in range(4):
            if grid[i][j]>=32: 
                return True
    return False 



def copy_grid(grid):
    grid2=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]] 
    for i in range(4):
        for j in range(4):
            grid2[i][j] = grid[i][j] 
    return grid2 

def grid_equal(a,b):
    if a==b:
        return True
    else:
        return False 