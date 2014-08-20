#def find_zero(i, position):
    

def push_up(grid):
    '''merge grid values upwards'''
    for i in range(4):
        for position in range (4):
            if i!= 3 and grid [i][position]==grid[i+1][position]:
                grid[i][position]=grid[i][position]*2
                grid[i+1][position]=0
                
    for i in range (4):
        for j in range(4):
            if grid[i][j]==0:
                if i!=3 and grid[i+1][j]!=0:
                    grid[i][j]=grid[i+1][j]
                elif i<2 and grid[i+2][j]!=0:
                    grid[i][j]=grid[i+2][j]
                elif i<1 and grid[i+3][j]!=0:
                    grid[i][j]=grid[i+3][j]
            
    return grid
                