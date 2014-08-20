#Kalind Ramnarayan
#29 April 2014
#merging grid values

def push_up (grid):
    """merge grid values upwards"""    
    
    for column in range(4):
        tempCol=[]
        for row in range(4):
            tempCol.append(grid[row][column])
    
        merge(tempCol)        
           
        for row in range(4):
            grid[row][column]=tempCol[row]
    
    
  
def push_down (grid):
    for column in range(4):
        grid[3][column],grid[0][column]=grid[0][column],grid[3][column]
        grid[1][column],grid[2][column]=grid[2][column],grid[1][column]
    
    push_up(grid)
    
    for column in range(4):
        grid[3][column],grid[0][column]=grid[0][column],grid[3][column]
        grid[1][column],grid[2][column]=grid[2][column],grid[1][column]
    
    
def push_left (grid):
    """merge grid values left"""
    for row in range(4):
            tempRow=[]
            for column in range(4):
                tempRow.append(grid[row][column])
            
            merge(tempRow)
            
            for column in range(4):
                grid[row][column]=tempRow[column]
            


def push_right (grid):
    """merge grid values right"""  
    for row in range(4):
            grid[row][0],grid[row][3]=grid[row][3],grid[row][0]
            grid[row][1],grid[row][2]=grid[row][2],grid[row][1]    

    push_left(grid)
    
    for row in range(4):
            grid[row][0],grid[row][3]=grid[row][3],grid[row][0]
            grid[row][1],grid[row][2]=grid[row][2],grid[row][1]    
    

def merge(lst):
    for number in lst:
        if number==0:
            lst.remove(number)
            lst.append(0)
       
    for i in range(3):
        if lst[i]==lst[i+1]:
            lst[i]=lst[i]+lst[i+1]
            lst.remove(lst[i+1])
            lst.append(0)        
            
            
            
            
