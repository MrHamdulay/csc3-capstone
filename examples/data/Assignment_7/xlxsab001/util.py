import copy

def create_grid(grid):
    for i in range(4):
        grid.append([0,0,0,0])
    return grid
           
        

def print_grid(grid):
    
    print("+","-"*20,"+",sep="")
    for i in range (4):
        print("|",end="")
        for j in range (4):
            if grid[i][j]!=0:
                print ("{0:<5}".format(grid[i][j]),end="")
            else:
                print ("{0:<5}".format(" "),end="")
        print("|")
    print("+","-"*20,"+",sep="")
        
def check_lost(grid):
    truecount=0
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j]==0:
                truecount+=1
            if grid[i][j]==grid[i][j-1]:
                truecount+=1
    
    if truecount>0:
        return False
    else:
        return True
                
                
def check_won(grid):
    wincheck=0
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j]>31:
                wincheck+=1
              
    if wincheck==0:
        return False
    else:
        return True
    
def copy_grid(grid):
    newgrid=[[] for i in range(4)]
    for i in range (4):
        for j in range (4):
            newgrid[i].append(grid[i][j])
    return newgrid
        
  
            
def grid_equal(grid1,grid2):
    eqcount=0
    for i in range(len(grid1)):
        for j in range(len(grid2)):
            if grid1[i][j]==grid2[i][j]:
                eqcount+=1
                
    if eqcount==16:
        return True
    else:
        return False
    