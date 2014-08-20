"""question 2-assignment 7- grids
GVNPRI022
02 May 2014"""
grid=[]
def create_grid(grid):
    
    #column= [0,0,0,0]
    for i in range(4):
        grid.append([0]*4)
    
    return grid

def print_grid(grid):
    """for x in range(len(grid)):
        for y in range(len(grid[x])):
            
            if grid[x][y]==0:
                grid[x][y]=" " """
    for i in range(6):
        if (i==0 or i==5):
            print("+"+20*"-"+"+") #print initial and end characters
        
        else:
            for j in range(4):
                if(grid[i-1][j]==0):
                    grid[i-1][j]=" "    
            l= "|{0:<5}{1:<5}{2:<5}{3:<5}|".format(grid[i-1][0],grid[i-1][1],grid[i-1][2],grid[i-1][3]) #formatting each line (for 5 character width)
            print(l)
            for j in range(4):
                if(grid[i-1][j]==" "):
                    grid[i-1][j]=0            
        
def check_lost(grid):
    tk= True #boolean conditional variable
    for x in range(1,4):
        for y in range(1,4):
            if (grid[x][y]==0 or grid[x][y]==grid[x-1][y] or grid[x][y]==grid[x][y-1]or grid[0][y]==0 or grid[x][0]==0 or grid[0][0]==0):#last 3 conditions to check for values that the loop doenst cover
                tk= False
                break
                
    
    if (tk==True):
        return True
    else:
        return False
    

    
        
        
         
def check_won(grid):
    tk= False
    for x in range(len(grid)):
        for y in range(len(grid[x])):    
            if (grid[x][y]>=32):
                tk=True
                return True
    
    if (tk==False):
        return False
    
def copy_grid(grid):
    gridCopy = [row[:] for row in grid] #code to copy array whilst not being affected by original array manipulation
    
    
    return gridCopy

def grid_equal(grid1,grid2):
    if(grid1==grid2):
        return True
    else:
        return False
   

    
    
            