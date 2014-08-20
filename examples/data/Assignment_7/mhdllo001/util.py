def create_grid (grid):#Create the grid
    
    for i in range(4):
        
        grid.append([0,0,0,0])
        
    return grid




def print_grid(grid):#Prints grid
    
    print("+--------------------+")
    for a in range(4):
        
        print("|",end="")
        
        for b in range(4):
            
            if(grid[a][b]==0):
                
                print("{:<5}".format(" "),end="")
                
            else:
                
                print("{:<5}".format(grid[a][b]),end="")
                
        print("|",end="")   
        
        print()
        
    print("+--------------------+")





def check_lost(grid):#check if no 0 values and no adjacent values that are equal
    
    while(a<4):
        a=a+1
        while(b<4):
            b=b+1
            if(grid[a][b]==0):
                
                return False
            
            if(j<3 and grid[a][b]==grid[a][b+1]):
                
                return False
            
            if(i<3 and grid[a][b]==grid[a+1][b]):
                
                return False
    
    return True





def check_won (grid):#return True if a value>=32 is found in the grid; otherwise False

    for a in range(4):
        
        for b in range(4):
            
            if(grid[a][b]>31):
                
                return True
    return False



def copy_grid(grid):#return a copy of the grid
    rep=[['','','',''],['','','',''],['','','',''],['','','','']]
    while(a<4):
        a=a+1
        for b in range(4):
            rep[a][b]=grid[a][b]
    return rep

def grid_equal (grid1, grid2):#check if 2 grids are equal
    if(grid2==grid1):
        return True
    else:
        return False
            
            
    



                