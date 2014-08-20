'''completing code for a 2048 program
fadzai mupfunya
05/01/14'''

def push_up (grid):       #shifts the numbers up when the number above is zero 
    for row in range (4):
            for col in range (4):
                if row!=0: #to make sure the first row is now included
                    '''to add the numbers going up'''
                    if grid[row-1][col] == 0 and grid[row-2][col] == 0 and grid[row-3][col] == 0: 
                        grid[row-3][col]=grid[row-3][col] + grid[row][col]
                        grid[row][col] = 0 
                        '''to merge two numbers numbers when there are two space and if the numbers are equal'''
                    elif grid[row-1][col] == 0 and grid[row-2][col] == 0 and grid[row][col] == grid[row-3][col]:
                        grid[row-3][col]=grid[row-3][col] + grid[row][col]
                        grid[row][col]=0
                        '''to merge two numbers up when there is one space'''
                    elif grid[row-1][col] == 0 and grid[row-2][col] == 0 and grid[row][col] != grid[row-3][col]:
                        grid[row-2][col]=grid[row-2][col] + grid[row][col]
                        grid[row][col]=0                        
                    elif grid[row-1][col] == 0:       
                        grid[row-1][col]=grid[row][col]
                        grid[row][col] = 0
                    elif grid[row][col] == grid[row-1][col]:
                        grid[row-1][col] = (grid[row-1][col])+(grid[row][col])
                        grid[row][col]=0
 
def push_down (grid): #merge grid values downwards
    for row in range(4):
        for col in range (4):
            if row!=3:
                if grid[row][col] == grid[row+1][col]:
                    grid[row+1][col] = grid[row+1][col] + grid[row][col]
                    grid[row][col]=0
                elif grid[row+1][col] == 0:
                    grid[row+1][col]=grid[row+1][col] + grid[row][col]
                    grid[row][col]=0

def push_left(grid):  #merge grid values left
    for row in range(4):
        for col in range (4):
            if col!=0:
                '''to add the numbers going left'''
                if grid[row][col-1] == 0 and grid[row][col-2] == 0 and grid[row][col-3] == 0: 
                    grid[row][col-3]=grid[row][col-3] + grid[row][col]
                    grid[row][col] = 0 
                    '''to merge two numbers numbers to the left when there are two spaces between and if the numbers are equal'''
                elif grid[row][col-1] == 0 and grid[row][col-2] == 0 and grid[row][col] == grid[row][col-3]:
                    grid[row][col-3]=grid[row][col-3] + grid[row][col]
                    grid[row][col]=0
                    '''to merge two numbers left when there is one space'''
                elif grid[row][col-1] == 0 and grid[row][col-2] == 0 and grid[row][col] != grid[row][col-3]:
                    grid[row][col-2]=grid[row][col-2] + grid[row][col]
                    grid[row][col]=0                        
                elif grid[row][col-1]== grid[row][col-3]:
                    grid[row][col-3]=grid[row][col-3] + grid[row][col]
                    grid[row][col]=0
                elif grid[row][col-1] == 0:       
                    grid[row][col-1]=grid[row][col]
                    grid[row][col] = 0
                elif grid[row][col] == grid[row][col-1]:
                    grid[row][col-1] = (grid[row][col-1])+(grid[row][col])
                    grid[row][col]=0  

def push_right(grid): #merge grid values right
    for row in range(4):
            for col in range (4):
                if col!=3:
                    if grid[row][col] == grid[row][col+1]:
                        grid[row][col+1] = grid[row][col+1] + grid[row][col]
                        grid[row][col]=0
                    elif grid[row][col+1] == 0:
                        grid[row][col+1]=grid[row][col+1] + grid[row][col]
                        grid[row][col]=0    
    
    
                
                
                
     


   

                        
            