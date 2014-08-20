#Lauren de Bruyn
#Merging grid values up, down, left and right
#1 May 2014

def push_up (grid):
    """merge grid values upwards"""
#move values upwards    
    for column in [0,1,2,3]:
        for row in [2,1,0]:
            if grid[row][column]==0:
                for i in range(row,3):
                    grid[i][column]= grid[i+1][column]
                grid[3][column]=0
    
#merge values that are equal together    
    for column in [0,1,2,3]:
        for row in [0,1,2]:
            if grid[row][column]==grid[row+1][column]:
                grid[row][column]=grid[row][column]*2
                for i in range(row,2):
                    grid[i+1][column]=grid[i+2][column]
                grid[3][column]=0
                
    
def push_down (grid):
    """merge grid values downwards"""
#move values downwards
    for column in [0,1,2,3]:
        for row in [1,2,3]:
            if grid[row][column]==0:
                for i in range(row,0, -1):
                    grid[i][column]= grid[i-1][column]
                grid[0][column]=0

#merge values that are equal together        
    for column in [0,1,2,3]:
        for row in [3,2,1]:
            if grid[row][column]==grid[row-1][column]:
                grid[row][column]=grid[row][column]*2
                for i in range(row,1,-1):
                    grid[i-1][column]=grid[i-2][column]
                grid[0][column]=0    
    
def push_left (grid):
    """merge grid values left"""
#move values leftwards
    for row in [0,1,2,3]:
        for column in [2,1,0]:
            if grid[row][column]==0:
                for i in range(column,3):
                    grid[row][i]= grid[row][i+1]
                grid[row][3]=0

 #merge values that are equal together
    for row in [0,1,2,3]:
        for column in [0,1,2]:
            if grid[row][column]==grid[row][column+1]:
                grid[row][column]=grid[row][column]*2
                for i in range(column,2):
                    grid[row][i+1]=grid[row][i+2]
                grid[row][3]=0     

def push_right (grid):
    """merge grid values right"""   
#move values rightwards    
    for row in [0,1,2,3]:
            for column in [1,2,3]:
                if grid[row][column]==0:
                    for i in range(column,0, -1):
                        grid[row][i]= grid[row][i-1]
                    grid[row][0]=0

#merge values that are equal together            
    for row in [0,1,2,3]:
        for column in [3,2,1]:
            if grid[row][column]==grid[row][column-1]:
                grid[row][column]=grid[row][column]*2
                for i in range(column,1,-1):
                    grid[row][i-1]=grid[row][i-2]
                grid[row][0]=0    