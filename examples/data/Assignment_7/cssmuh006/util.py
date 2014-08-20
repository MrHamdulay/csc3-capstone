def create_grid(grid):
    #create a 4x4 grid
    for i in range(4):
        grid.append([0,0,0,0])
        
def print_grid(grid):
    #print grid
    for i in range(-1,len(grid)+1):
        
        if 0<=i<=len(grid)-1:
            print("|",sep="",end="")
            for j in range(len(grid[i])):
                p=str(grid[i][j])
                if p=="0":
                    p=""
                print(p," "*(5-len(p)),sep="",end="")
            print("|")
        
        else:
            print("+","-"*20,"+",sep="")
            
def check_lost(grid):
    #check if player lost
    lost=True
    for j in range(len(grid)):
        
        for i in range(len(grid[j])):
            
            if(grid[j][i]==0):#if a tile is zero not lost
                lost=False
                
            else:
                up=j-1
                down=j+1
                left=i-1
                right=i+1
                #check above below right and left for equal values
                if(up<0):
                    if(grid[j][i]==grid[down][i]):
                        lost=False
                elif(down>(len(grid)-1)):
                    if(grid[j][i]==grid[up][i]):
                        lost=False
                else:
                    if(grid[j][i]==grid[up][i] or grid[j][i]==grid[down][i]):
                        lost=False
                        
                if(left<0):
                    if(grid[j][i]==grid[j][right]):
                        lost=False
                elif(right>(len(grid[j]))-1):
                    if(grid[j][i]==grid[j][left]):
                        lost=False
                else:
                    if(grid[j][i]==grid[j][left] or grid[j][i]==grid[j][right]):
                        lost=False                    
    return lost

def check_won(grid):
    #check if player won
    won=False
    for j in range(len(grid)):
        for i in range(len(grid[j])):
            if(grid[j][i]>=32):
                won=True
                
    return won

def copy_grid(grid):
    #copy grid values into a new grid
    copy=[[0, 0, 0, 0],[0, 0, 0, 0],[0, 0, 0, 0],[0, 0, 0, 0]]
    
    for i in range(len(copy)):
        for j in range(len(copy[i])):
            copy[i][j]=grid[i][j]
            
    return copy

def grid_equal(grid1,grid2):
    #check if 2 grids are equal
    equal=True
    for i in range(len(grid1)):
        for j in range(len(grid1[i])):
            if(grid1[i][j]!=grid2[i][j]):
                equal=False
                
    return equal
            