"""Assignment 9
DAnsonmasuka
14 May 2014"""

grid=[]  # create empty sudoku list                                                         
for i in range(9):                                                  
    i=input("")                                                     
    row=[] # create empty row
    for j in range(9):
        row.append(i[j])
    grid.append(row)

def checking1(grid): 
    """checks to see if more than one of same num is in the same row"""
    for row in range(9):                                            
        for checking1 in range(1,10):                                 
            if grid[row].count(str(checking1))>1:                   
                return False                                        
    else: return True                                               

def checking2(grid): 
    """checks to see if more than one of same num is in the col"""
    for col in range(9):                                         
        for row in range(8):                                        
            for checking2 in range(row+1,9):                          
                if grid[row][col]==grid[checking2][col]:    
                    return False                                    
    else: return True                                              

def checking3(grid): 
    """checks to see if any of the same num is within the smaller 3x3 grid"""
    for i in range(3):                                        
        for j in range(3):                                    
            grid=[]                                                 
            for row in range((3*i),(3*(i+1))):          
                for col in range((3*j),(3*(j+1))):   
                    grid.append(grid[row][col])                
            for num in range(1,10):                              
                if grid.count(str(num))>1:                       
                    return False                                    
    else: return True                                               

if checking1(grid) and checking2(grid) and checking3(grid):         
    print("Sudoku grid is valid")                                   
else:                                                              
    print("Sudoku grid is not valid")                               