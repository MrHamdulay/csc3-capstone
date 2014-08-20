def create_grid(grid):
    """create a 4x4 grid"""
    for i in range(4):
        grid.append([0,0,0,0])
    return grid

def print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    print("+","-"*20,"+",sep="")
    for i in range (len(grid)):
        for j in range (4):
            if(j==0):
                if grid[i][j]==0:
                    print("|"," "*5,sep="",end="")
                else:
                    print("|",grid[i][j]," "*(5-len(str(grid[i][j]))),sep="",end="")
            
            elif(j==3):
                if grid[i][j]==0:
                    print(" "*5,"|",sep="",end="")
                else:
                    print(grid[i][j]," "*(5-len(str(grid[i][j]))),"|",sep="",end="")
            else:
                if grid[i][j]==0:
                    print(" "*5,sep="",end="")
                else:
                    print (grid[i][j]," "*(5-len(str(grid[i][j]))),sep="",end="")
                
        print()        
    print("+","-"*20,"+",sep="")

def check_lost (grid):
    """return True if there are no 0 values and no adjacent values that are equal; otherwise False"""
    count=0
    for i in range (len(grid)):
        for j in range(4):
            if(grid[i][j]==0):
                count+=1
            if(j!=3):
                if(grid[i][j]==grid[i][j+1]):
                    count+=1
            if(i!=0):
                if(grid[i][j]==grid[i-1][j]):
                    count+=1
            
                
            
    if(count>0):
        return False
    else:
        return True

def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise False"""
    count = 0
    for i in range (len(grid)):
        for j in range(4):
            if(grid[i][j]>=32):
                count +=1
    if(count>0):
        return True
    else:
        return False
               

def copy_grid (grid):
    """return a copy of the grid"""
    grid2=[]
    grid2 = create_grid(grid2)
    for i in range (len(grid)):
        for j in range(4):
            grid2[i][j]=(grid[i][j])
    return grid2

def grid_equal (grid1, grid2):

    if grid1==grid2:
        return True
    else:
        return False
            
    
    
    