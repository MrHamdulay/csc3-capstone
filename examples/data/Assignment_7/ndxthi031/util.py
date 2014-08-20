#Thiolan Prevan Naidoo
#NDXTHI031
#question2_Util  
#Performs operations with a 4x4 grid

def create_grid(grid):
    for i in range(4):
        grid.append([0,0,0,0])#Creates a 4x4 grid of zeroes

        
def print_grid(grid):#prints grid
    grid1=list(grid)#creates a deepcopy of the grid
    for i in range(4):
        for j in range(4):
            if grid[i][j]==0:#changes all zeroes to spaces in order to print the grid without zeroes
                grid1[i][j]=""    
                
                
    print("+",20*"-","+",sep="")
    print("|","{0:<5}{1:<5}{2:<5}{3:<5}".format(grid1[0][0],grid1[0][1],grid1[0][2],grid1[0][3]),"|",sep="")
    print("|","{0:<5}{1:<5}{2:<5}{3:<5}".format(grid1[1][0],grid1[1][1],grid1[1][2],grid1[1][3]),"|",sep="")
    print("|","{0:<5}{1:<5}{2:<5}{3:<5}".format(grid1[2][0],grid1[2][1],grid1[2][2],grid1[2][3]),"|",sep="")
    print("|","{0:<5}{1:<5}{2:<5}{3:<5}".format(grid1[3][0],grid1[3][1],grid1[3][2],grid1[3][3]),"|",sep="")
    print("+",20*"-","+",sep="")
    
def check_lost(grid):#checks if the player has lost the game
    a=True
    b=True
    c=True
    for i in range(4):
        for j in range(4):
            if grid[i][j]==0:#changes a to false if any zero is found in the grid
                a=False
    
    for k in range(4):
        for l in range(3):
            if grid[k][l]==grid[k][l+1]:#changes b to false if any numbers to the left or right of each other are equal
                b=False
                
    for x in range(3):
        for y in range(4):
            if grid[x][y]==grid[x+1][y]:#changes c to false if any numbers above or below each other are equal
                c=False
    if a and b and c:
        return True
    else:
        return False
    
def check_won(grid):#checks if the player won the game by changing a to true if any value >=32 is found in the grid
    a=False
    for i in range(4):
        for j in range(4):
            if grid[i][j]>=32:
                a=True
    return a

def copy_grid(grid): #creates a copy of the grid
    Ngrid=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]#creates a new grid
    for i in range(4):
        for j in range(4):
            Ngrid[i][j]=grid[i][j]#assigns each value in the new grid to the corresponding value in the original grid
    
    
    
    return Ngrid

def grid_equal(grid1,grid2):#checks if two grids are equal
    if grid1==grid2:
        return True
    else:
        return False