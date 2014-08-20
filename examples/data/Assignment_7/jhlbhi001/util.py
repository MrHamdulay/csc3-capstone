def create_grid(grid):
    for i in range(4):
        grid.append ([0]*4)
    return grid
    
def print_grid(grid):
    print("+--------------------+")
    
    for i in range(4):
        print("|", end="")
        for j in range(4):
            if str(grid[i][j])=="0":
                print(" "*5,end="")
            else:
                print("{0:<5}".format(str(grid[i][j])), end="")
            
        print("|")
    print("+--------------------+")
    
def check_lost(grid):
    for i in range(4):
        for j in range(4):
            if str(grid[i][j])==0:
                return False
            elif j+1<4 and str(grid[i][j])==str(grid[i][j+1]):
                return False
            elif i+1<4 and str(grid[i][j])==str(grid[i+1][j]):
                return False
            
    return True

def check_won(grid):
    for i in range(4):
        for j in range(4):
            if str(grid[i][j])>="32":
                return True
            else:
                return False

def copy_grid(grid):
    grid1=[]
    for i in range(4):
        a=[]
        for j in range(4):
            a.append(grid[i][j])
        grid1.append(a)
    return grid1
    
def grid_equal(grid1,grid2):
    for i in range(4):
        for j in range(4):
            if str(grid1[i][j])==str(grid2[i][j]):
                return True
            else:
                return False

               
    
    

            
            
                     
            
        
        
            
            
            
            
    
            
            
            
        
        


        