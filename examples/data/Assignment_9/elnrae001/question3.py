'''Program to check if a sudoku grid is valid
Author:Raees Eland
Date:11 May 2014'''
        
def check_col(grid):
    '''check each column'''
    for col in range(9):
        new_grid=[] # after program checks a column new_grid becomes empty
        for row in range(9):
            if grid[row][col] not in new_grid:
                new_grid.append(grid[row][col])
            else:
                return False
    return True   
               
def check_row(grid):
    '''check each row'''
    for row in range(9):
        for i in grid[row]:
            if grid[row].count(i) > 1:
                return False
    return True
            
                
def check_3x3(grid):
    '''check each 3x3 grid'''
    for i in grid:
        if grid.count(i) > 1:
            return False
    return True
            
grid=[]
for i in range(9):
    grid.append([0]*9)# creates 9x9 grid
                        
#assign each value of the sudoku grid to the grid created    
for i in range(9):
    numbers=input()# input the sudoku grid
    for j in range(9):
        grid[i][j]=numbers[j]
        
# creates 9 3x3 grids from the 9x9 grid        
grid1=[]
for i in range(0,3):
    for j in range(0,3):
        grid1.append(grid[i][j])
        
grid2=[]
for i in range(0,3):
    for j in range(3,6):
        grid2.append(grid[i][j]) 
        
grid3=[]
for i in range(0,3):
    for j in range(6,9):
        grid3.append(grid[i][j])
        
grid4=[]
for i in range(3,6):
    for j in range(0,3):
        grid4.append(grid[i][j])
        
grid5=[]
for i in range(3,6):
    for j in range(3,6):
        grid5.append(grid[i][j])
        
grid6=[]
for i in range(3,6):
    for j in range(6,9):
        grid6.append(grid[i][j]) 
        
grid7=[]
for i in range(6,9):
    for j in range(0,3):
        grid7.append(grid[i][j])
        
grid8=[]
for i in range(6,9):
    for j in range(3,6):
        grid8.append(grid[i][j])
        
grid9=[]
for i in range(6,9):
    for j in range(6,9):
        grid9.append(grid[i][j])
        
if check_col(grid) and check_row(grid) and check_3x3(grid1) and check_3x3(grid2) and check_3x3(grid3) and check_3x3(grid4) and check_3x3(grid5) and check_3x3(grid6) and check_3x3(grid7) and check_3x3(grid8) and check_3x3(grid9):
    print('Sudoku grid is valid')
else:
    print('Sudoku grid is not valid')