"""prgramme to be tested in question
Karidas Tshintsholo
29-04-2014"""

#tshkar003

def create_grid(grid):
    ht=4
    for j in range(ht):
        grid.append([0]*4)


def print_grid(grid):
    print("+","-"*20,"+",sep="") 
    height=4
    for j in range(ht):
        grid.append([0]*4) 
    for row in range(ht):
        print("|",end="") 
        for column in range(ht):
            if grid[row][column]==0: 
                print(" ".ljust(5),end="") 
            else:
                print(str((grid[row][column])).ljust(5),end="") 
        print("|",end="") 
        print()
    
    print("+","-"*20,"+",sep="") 


def check_lost(grid):
    
    for row in range(4):
        for column in range(4):
            if grid[row][column]==0:
                return False
            else:
                if row-1 >= 0: 
                    if grid[row-1][column]==grid[row][column]: 
                        return False
                if row+1<=3: 
                    if grid[row+1][column]==grid[row][column]:  
                        return False
                if column-1>=0:
                    if grid[row][column-1]==grid[row][column]: 
                        return False
                if column+1<=3: 
                    if grid[row][column+1]==grid[row][column]: 
                        return False
    return True 


def check_won(grid):
    #print(grid)
    for row in range(4):
        for column in range(4):
            if grid[row][column]>=32: 
                return True
    return False 



def copy_grid(grid):
    gridNew=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]] 
    for row in range(4):
        for column in range(4):
            gridNew[row][column] = grid[row][column] 
    return gridNew 

def grid_equal(grid1,grid2):
    if grid1==grid2:
        return True
    else:
        return False
            
    
    

                