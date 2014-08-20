def create_grid(grid):
        for i in range(4):
                grid.append([0,0,0,0])   
        #grid=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        return grid
            
def print_grid (grid):
        print("+--------------------+")
        for i in range(4):
                print("|",end="")
                for j in range(4):
                        if grid[i][j]==0:
                                grid[i][j]=" "
                        print(grid[i][j],end=" "*(5-(len(str(grid[i][j])))))
                        if grid[i][j]==" ":
                                grid[i][j]=0
                print("|")
                print("",end="")       
        print("+--------------------+")

def check_lost(grid):
        adjacent=0
        adjacent2=0
        for i in range(4):
                if 0 in grid[i]:
                        return False
        else:
                for j in range(4):
                        for h in range(4):
                                if grid[j][0]==grid[j][1] or grid[j][1]==grid[j][2] or grid[j][2]==grid[j][3]:
                                        adjacent+=1
                                if grid[0][h]==grid[1][h] or grid[1][h]==grid[2][h] or grid[2][h]==grid[3][h]:
                                        adjacent2+=1
                if adjacent==0 and adjacent2==0:
                        return True
                else:
                        return False
def check_won(grid):
        x=0
        for i in range(4):
                for j in range(4):
                        if grid[i][j]>=32:
                                x+=1
        if x>=1:
                return True
        else:
                return False
                                
def copy_grid(grid):
        import copy
        copyofgrid = copy.deepcopy(grid)
        return copyofgrid

def grid_equal(grid1,grid2):
        if grid1==grid2:
                return True
        else:
                return False
        
        
#grid =[]
#create_grid(grid)
#print(grid)
        
         